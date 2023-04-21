import json
import time
from time import perf_counter
from datetime import datetime
import click
import cloup
from cloup import option, option_group
from cloup.constraints import mutually_exclusive

import keyring

from github import Github

from .deployment import all_deployments_completed
from .workflow import all_runners_completed


def login() -> Github:
    github_token = keyring.get_password("gunner", "TOKEN")
    if not github_token:
        raise
    gh = Github(login_or_token=github_token)
    return gh


# Command Group
@cloup.group(name="get")
def getter():
    """Tool related commands"""
    pass


@getter.command(
    name="all_deployments", help="get a list of deployments", no_args_is_help=True
)
@option("--owner", required=True, help="repository owner - organization")
@option("--repository", required=True, help="repository name")
@option("--task", required=False, help="task name - e.g. job name")
@option_group(
    "reference to commit or tag",
    option("--tag", required=False, help="full tag name"),
    option("--sha", required=False, help="git commit hash"),
    constraint=mutually_exclusive,
)
@option(
    "--created_at_from", required=False, help="search from one date YYYY-MM-DD HH:MM:SS"
)
@option("--created_at_to", required=False, help="search to date YYYY-MM-DD HH:MM:SS")
@option(
    "--wait-all",
    required=False,
    type=bool,
    default=False,
    help="wait until all tasks are finished.",
)
@option(
    "--wait-time",
    required=False,
    type=int,
    default=10,
    help="number of seconds to wait after each request",
)
@option(
    "--minimum-wait-time",
    required=False,
    type=int,
    default=0,
    help="wait a minimum of K seconds, to see if status changes.",
)
def all_deployments(
    owner: str,
    repository: str,
    task: str,
    tag: str,
    sha: str,
    created_at_from: datetime,
    created_at_to: datetime,
    wait_all: str,
    wait_time: int,
    minimum_wait_time: int,
):
    kwargs = {}
    if task:
        kwargs["task"] = task
    if tag:
        kwargs["ref"] = tag
    if sha:
        kwargs["sha"] = sha

    if created_at_from:
        created_at_from: datetime = datetime.strptime(  # type: ignore[no-redef]
            created_at_from, "%Y-%m-%d %H:%M:%S"
        )
    if created_at_to:
        created_at_to: datetime = datetime.strptime(  # type: ignore[no-redef]
            created_at_to, "%Y-%m-%d %H:%M:%S"
        )

    gh = login()
    deployments_running = True
    filter = {}
    start_time = perf_counter()

    while deployments_running:
        completed, statuses, deployments = all_deployments_completed(
            gh,
            owner,
            repository,
            created_at_from,
            created_at_to,
            filter,
            **kwargs,
        )
        elapsed_time = perf_counter() - start_time
        # used to wait for the workflows to finish
        if (wait_all and not completed) or (
            minimum_wait_time > 0 and elapsed_time <= minimum_wait_time
        ):
            time.sleep(wait_time)
        # used to wait wait for the workflow to start.
        elif not wait_all or (
            minimum_wait_time > 0 and elapsed_time > minimum_wait_time
        ):
            deployments_running = not completed

        if (not wait_all) or (wait_all and completed):
            deployments_serialized = [deployment.raw_data for deployment in deployments]
            status_values = set(statuses.values())
            all_success = len(status_values) == 1 and "success" in status_values
            click.echo(
                json.dumps(
                    {
                        "deployments": deployments_serialized,
                        "statuses": statuses,
                        "all_completed": completed,
                        "all_success": all_success,
                    },
                    indent=2,
                )
            )
            return


# minimum wait time
# time between pings
@getter.command(
    name="watch_deployments",
    help="watch specific runners until all are in finite state.",
    no_args_is_help=True,
)
@click.option("--workflow_id", required=False, help="runner_id of github action")
@click.option("--tag", required=False, help="full tag name")
@click.option("--sha", required=False, help="git commit hash")
@click.option(
    "--event",
    required=False,
    help="""events that trigger workflow
    full list:
    https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows""",
)
@click.option(
    "--output",
    default="status",
    help="""possible options is to get cli to return deployment status using 'status'
     or json with 'json'""",
)
@click.option(
    "--from_date",
    required=False,
    help="UTC date - created date for when it was triggered. Can include timestamp",
)
@click.option(
    "--to_date",
    required=False,
    help="UTC date - created date for when it was triggered. Can include timestamp",
)
def filtered_deployments(**kwargs):
    click.echo(f"filtered runners: {kwargs}")


@getter.command(name="all_runners", help="get a list of runner", no_args_is_help=True)
@option("--owner", required=True, help="repository owner - organization")
@option("--repository", required=True, help="repository name")
@option(
    "--actor",
    required=False,
    help="Returns someone's workflow runs. Use the login for the user who created the push associated with the check suite or workflow run.",
)
@option(
    "--branch", required=False, help="the specific branch the runner is attached to."
)
@option("--event", required=False, help="event triggering the workflow. e.g. push")
@option("--tag", required=False, help="filter workflow runners by tag or branch")
@option(
    "--created_at_from", required=False, help="search from one date YYYY-MM-DD HH:MM:SS"
)
@option("--created_at_to", required=False, help="search to date YYYY-MM-DD HH:MM:SS")
@option(
    "--wait-time",
    required=False,
    type=int,
    default=10,
    help="number of seconds to wait after each request",
)
@option(
    "--status",
    required=False,
    type=click.Choice(
        [
            "completed",
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "skipped",
            "stale",
            "success",
            "timed_out",
            "in_progress",
            "queued",
            "requested",
            "waiting",
            "pending",
        ]
    ),
    help="the type of statuses to search for",
    multiple=True,
)
@option(
    "--wait-all",
    required=False,
    type=bool,
    default=False,
    help="wait until all tasks are finished.",
)
@option(
    "--minimum-wait-time",
    required=False,
    type=int,
    default=0,
    help="wait a minimum of K seconds, to see if status changes.",
)
def all_runners(
    owner: str,
    repository: str,
    actor: str,
    branch: str,
    status: list[str],
    event: str,
    tag: str,
    created_at_from: str,
    created_at_to: str,
    wait_all: bool,
    wait_time: int,
    minimum_wait_time: int,
):
    """_summary_

    :param owner: owner e.g. google
    :type owner: str
    :param repository: repository e.g. ghunner
    :type repository: str
    :param actor: the user that created the push.
    :type actor: str
    :param branch: branch or tag to search for.
    :type branch: str
    :param status: status e.g. failure, success, in-progress ++
    :type status: list[str]
    :param event: type of event e.g. push
    :type event: str
    :param tag: filter on tag
    :type tag: str
    :param created_at_from: date to start filtering from
    :type created_at_from: str
    :param created_at_to: date to end filtering
    :type created_at_to: str
    :param wait_all: wait on all to complete.
    :type wait_all: bool
    :param wait_time: wait time, is the time to wait if they are not completed.
    :type wait_time: int
    """
    kwargs = {}
    if actor:
        kwargs["actor"] = actor
    if branch:
        kwargs["branch"] = branch
    if status and len(status) == 1:
        kwargs["status"] = status[0]
    if event:
        kwargs["event"] = event

    filter = {}
    if tag:
        filter["head_branch"] = tag

    if status and len(status) > 1:
        filter["statuses"] = status  # type: ignore
    if created_at_from:
        created_at_from: datetime = datetime.strptime(  # type: ignore[no-redef]
            created_at_from, "%Y-%m-%d %H:%M:%S"
        )
    if created_at_to:
        created_at_to: datetime = datetime.strptime(  # type: ignore[no-redef]
            created_at_to, "%Y-%m-%d %H:%M:%S"
        )

    gh = login()
    workflows_running = True
    start_time = perf_counter()
    while workflows_running:
        running, workflow_runs = all_runners_completed(
            gh,
            owner,
            repository,
            created_at_from,
            created_at_to,
            filter,
            **kwargs,
        )

        elapsed_time = perf_counter() - start_time

        # used to wait for the workflows to finish
        if (wait_all and running) or (
            minimum_wait_time > 0 and elapsed_time <= minimum_wait_time
        ):
            time.sleep(wait_time)
        # used to wait wait for the workflow to start.
        elif not wait_all or (
            minimum_wait_time > 0 and elapsed_time > minimum_wait_time
        ):
            workflows_running = running

        if (not wait_all) or (wait_all and not running):
            workflow_runs_serialized = [workflow.raw_data for workflow in workflow_runs]
            statuses = [workflow.status for workflow in workflow_runs]
            conclusions = [workflow.conclusion for workflow in workflow_runs]
            conclusions_set = set(conclusions)
            all_success = "success" in conclusions_set and len(conclusions_set) == 1

            click.echo(
                json.dumps(
                    {
                        "workflow_runs": workflow_runs_serialized,
                        "statuses": statuses,
                        "conclusions": conclusions,
                        "all_completed": not running,
                        "all_success": all_success,
                    },
                    indent=2,
                )
            )
            return


if __name__ == "__main__":
    getter()

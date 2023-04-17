import typing
from datetime import datetime
from .helper import get_pages

from github.WorkflowRun import WorkflowRun
from github.PaginatedList import PaginatedList
from github import Github


def all_runners_completed(
    gh: Github,
    owner: str,
    repository: str,
    from_date: datetime,
    to_date: datetime,
    filter: dict[str, typing.Any],
    **kwargs: dict[str, typing.Any],
) -> tuple[bool, list[WorkflowRun]]:
    """Checks if all runners have completed or not.
       Also returns the workflows.


    :param gh: github object to perform requests.
    :type gh: Github
    :param owner: owner e.g. Google
    :type owner: str
    :param repository: repository name e.g. ghunner
    :type repository: str
    :param from_date: date to search from
    :type from_date: datetime
    :param to_date: date to search to
    :type to_date: datetime
    :param filter: filter on workflow variables.
    :type filter: dict[str, typing.Any]
    :return: all completed workflows as bool and workflow runs.
    :rtype: tuple[bool, list[WorkflowRun]]
    """

    workflow_runs_paged: PaginatedList[WorkflowRun] = gh.get_repo(
        f"{owner}/{repository}"
    ).get_workflow_runs(**kwargs)

    workflow_runs: list[WorkflowRun] = get_pages(  # type: ignore[assignment]
        workflow_runs_paged,
        from_date=from_date,
        to_date=to_date,
        filter=filter,
    )
    completed = is_worklow_runs_completed(workflow_runs)

    return completed, workflow_runs


def is_worklow_runs_completed(workflow_runs: list[WorkflowRun]) -> bool:
    """Checks if a workflow run status is finished or not.
       early return if one workflow is not completed.


    :param workflow_runs: workflow object
    :type workflow_runs: list[WorkflowRun]
    :return: if there is a workflow not completed.
    :rtype: bool
    """
    for workflow_run in workflow_runs:
        if workflow_run.status in [
            "in_progress",
            "queued",
            "requested",
            "waiting",
            "pending",
        ]:
            return False
    return True

import typing
from .helper import get_pages
from github.Deployment import Deployment
from github.DeploymentStatus import DeploymentStatus
from github.PaginatedList import PaginatedList
from github import Github
from datetime import datetime


def is_completed(deployment_statuses: list[DeploymentStatus]) -> bool:
    """checks if all deployments are completed

    :param deployment_statuses: list of deployments
    :type deployment_statuses: list[DeploymentStatus]
    :return: true/false if all deployments are completed.
    :rtype: bool
    """
    for deployment_status in deployment_statuses:
        if deployment_status.state in ["error", "failure", "inactive", "success"]:
            return True
    return False


def get_deployment_status(deployment_statuses: list[DeploymentStatus]) -> str:
    """Returns all statuses.
       if success return
       else return the first one.

    :param deployment_statuses: deployment status e.g. failure, success etc.
    :type deployment_statuses: list[DeploymentStatus]
    :return: the status of the deployment.
    :rtype: str
    """
    states = []
    for deployment_status in deployment_statuses:
        state = deployment_status.state
        if state != "success":
            states.append(state)
        else:
            return state
    return states[0]


def all_deployments_completed(
    gh: Github,
    owner: str,
    repository: str,
    from_date: datetime,
    to_date: datetime,
    filter: dict[str, typing.Any],
    **kwargs,
) -> tuple[bool, dict[int, str], list[Deployment]]:
    """gets all deployments, checks if they are completed

    :param gh: github object to search with
    :type gh: Github
    :param owner: owner of e.g. google
    :type owner: str
    :param repository: repository e.g. ghunner.
    :type repository: str
    :return: all completed, statuses of completion, list of deployments
    :rtype: tuple[bool, dict[int, str], list[Deployment]]
    """
    deployments_paged: PaginatedList = gh.get_repo(
        f"{owner}/{repository}"
    ).get_deployments(**kwargs)

    deployments: list[Deployment] = get_pages(
        deployments_paged, from_date=from_date, to_date=to_date, filter=filter
    )  # type: ignore
    completed = 0
    statuses = {}
    for deployment in deployments:
        deployment_statuses = deployment.get_statuses()
        if is_completed(deployment_statuses):
            completed += 1
            final_status = get_deployment_status(deployment_statuses)
            statuses[deployment.id] = final_status
    return len(deployments) == completed, statuses, deployments

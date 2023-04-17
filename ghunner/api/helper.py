from github.PaginatedList import PaginatedList
from datetime import datetime
from copy import deepcopy


def filter_objects(
    objects: list[object],
    filter: dict[str, str],
    from_date: datetime = None,
    to_date: datetime = None,
) -> list[object]:
    """This filter function could probably be cleaned up a bit.
        It works both on WorkflowRuns and Deployments.
        This is the reason is uses hasattr and getattr.

    :param objects: list of either WorkflowRun or Deployment
    :type objects: list[object]
    :param filter: dicitonary of variables to filter on.
    :type filter: dict[str, str]
    :param from_date: _description_, defaults to None
    :type from_date: datetime, optional
    :param to_date: _description_, defaults to None
    :type to_date: datetime, optional
    :return: _description_
    :rtype: list[object]
    """

    filter_list = []

    # done to be able to have filters that is used on more general things.
    # needs to delete filter keys before end of function in copy.
    # this is used to see if object should be added.
    filter_copy = deepcopy(filter)
    date_skip = False
    if filter is None:
        return objects, date_skip

    if "statuses" in filter_copy:
        filter_statuses = filter_copy["statuses"]
        del filter_copy["statuses"]
    for general_obj in objects:
        similar = 0
        if hasattr(general_obj, "created_at"):
            date = getattr(general_obj, "created_at")
            if from_date or to_date:
                if not (
                    (from_date and from_date <= date) or (to_date and date <= to_date)
                ):
                    date_skip = True
                    continue
        if hasattr(general_obj, "status") and hasattr(general_obj, "conclusion"):
            status = getattr(general_obj, "status")
            conclusion = getattr(general_obj, "conclusion")
            if status not in filter_statuses and conclusion not in filter_statuses:
                continue

        for variable, variable_value in filter_copy.items():
            if hasattr(general_obj, variable):
                object_value = getattr(general_obj, variable)
                if object_value == variable_value:
                    similar += 1
        if similar == len(filter_copy):
            filter_list.append(general_obj)

    return filter_list, date_skip


def get_pages(
    pages: PaginatedList,
    from_date: datetime = None,
    to_date: datetime = None,
    filter: dict[str, str] = None,
) -> object:
    """Function to transform paging to list.
       filter gives the ability to not have all pages
       returned.

       can also filter on dates.

    :param pages: _description_
    :type pages: PaginatedList
    :param from_date: date to filter from, defaults to None
    :type from_date: datetime, optional
    :param to_date: date to filter to, defaults to None
    :type to_date: datetime, optional
    :param filter: variables to filter on, defaults to None
    :type filter: dict[str, str], optional
    :return: list of workflow runs after filters were used.
    :rtype: object
    """
    total_count = pages.totalCount
    elements = []
    for i in range(total_count):
        tmp_elements = pages.get_page(i)
        filtered_elements, date_skip = filter_objects(
            tmp_elements, filter, from_date, to_date
        )
        elements += filtered_elements
        if date_skip:
            break
    return elements

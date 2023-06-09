from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    job_salaries = list()
    for job in jobs:
        if job["max_salary"].isnumeric():
            job_salaries.append(int(job["max_salary"]))
    return max(job_salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    job_salaries = list()
    for job in jobs:
        if job["min_salary"].isnumeric():
            job_salaries.append(int(job["min_salary"]))
    return min(job_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif isinstance(salary, int) is False and isinstance(salary, str) is False:
        raise ValueError
    elif (
        isinstance(job["min_salary"], int) is not True
        and isinstance(job["min_salary"], str) is not True
        or isinstance(job["max_salary"], int) is not True
        and isinstance(job["max_salary"], str) is not True
    ):
        raise ValueError
    elif int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered.append(job)
        except ValueError as e:
            print(e)
    return filtered

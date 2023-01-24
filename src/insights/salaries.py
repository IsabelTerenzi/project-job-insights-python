from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salaries = read(path)
    # A função deve obter os dados da mesma forma que o requisito 2
    salaries_set = set()
    for value in salaries:
        if value["max_salary"] != '' and value["max_salary"] != 'invalid':
            # a função deve ignorar os valores ausentes
            salaries_set.add(int(value["max_salary"]))
            # retornar um int com o maior salário da coluna max_salary
    return max(salaries_set)


def get_min_salary(path: str) -> int:
    salaries = read(path)
    # A função deve obter os dados da mesma forma que o requisito 2
    salaries_set = set()
    for value in salaries:
        if value["min_salary"] != '' and value["min_salary"] != 'invalid':
            # a função deve ignorar os valores ausentes
            salaries_set.add(int(value["min_salary"]))
            # retornar um int com o maior salário da coluna max_salary
    return min(salaries_set)


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
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
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
    raise NotImplementedError

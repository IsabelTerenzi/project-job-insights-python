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
            # retornar um int com o menor salário da coluna min_salary
    return min(salaries_set)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, (int, str))
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError

    if job["min_salary"] <= int(salary) <= job["max_salary"]:
        return True
    else:
        return False


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

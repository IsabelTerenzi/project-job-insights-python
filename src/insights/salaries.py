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
        or not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
        or not isinstance(salary, (int, str))
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    salaries_list = list()
    for value in jobs:
        try:
            if matches_salary_range(value, salary):
                salaries_list.append(value)
        except ValueError:
            pass
    return salaries_list

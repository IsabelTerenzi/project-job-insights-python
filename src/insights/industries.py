from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries = read(path)
    industries_set = set()
    for value in industries:
        if value['industry'] != '':
            # a função desconsidera valores vazios
            industries_set.add(value["industry"])
            # a função deve retornar uma lista de valores da coluna industry
    return list(industries_set)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError

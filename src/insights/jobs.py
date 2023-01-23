from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    # a função deve receber um path
    jobs = []
    with open(path, encoding="utf-8") as file:
        # a função deve abrir o arquivo e ler seus conteúdos (open, DictReader)
        jobs_content = csv.DictReader(file, delimiter=",", quotechar='"')
        # a função deve retornar uma lista de dicionários
        for value in jobs_content:
            jobs.append(value)
    return jobs


def get_unique_job_types(path: str) -> List[str]:
    # a função deve receber o path do arquivo csv
    types = read(path)
    # a função deve invocar a função jobs.read com o path
    types_set = set()
    for value in types:
        types_set.add(value['job_type'])
    # a função deve retornar uma lista de valores da coluna job_type
    return list(types_set)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

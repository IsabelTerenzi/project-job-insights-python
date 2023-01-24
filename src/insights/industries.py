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
    # A função recebe uma lista de dicionários como primeiro parâmetro
    # A função recebe uma string industry como segundo parâmetro
    industries_list = list()
    for value in jobs:
        if value["industry"] == industry:
            industries_list.append(value)
        # deve retornar uma lista da coluna industry
        # correspondente ao parâmetro industry
    return industries_list

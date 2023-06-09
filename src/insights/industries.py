from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    my_jobs = read(path)
    result = set()
    for job in my_jobs:
        unique_industries = job['industry']
        if unique_industries != '':
            result.add(unique_industries)
    return result


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    result = [list for list in jobs if list['industry'] == industry]
    return result

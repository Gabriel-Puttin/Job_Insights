import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = [rows for rows in jobs_reader]

    return jobs


def get_unique_job_types(path: str) -> List[str]:
    my_jobs = read(path)
    result = set()
    for job in my_jobs:
        unique_job_types = job['job_type']
        result.add(unique_job_types)
    return result


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    result = [list for list in jobs if list['job_type'] == job_type]
    return result

from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    my_jobs = read(path)
    result = 0
    for job in my_jobs:
        salary: str = job['max_salary']
        if salary.isdigit() and int(salary) > int(result):
            result = salary
    return int(result)


def get_min_salary(path: str) -> int:
    my_jobs = read(path)
    result = 50000
    for job in my_jobs:
        salary: str = job['min_salary']
        if salary.isdigit() and int(salary) < int(result):
            result = salary
    return int(result)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        if min_salary > max_salary:
            raise ValueError
        elif int(salary) in range(min_salary, max_salary):
            return True
        else:
            return False
    except (TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    result = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary) is True):
                result.append(job)
        except ValueError:
            print('Arguments must be valids')
    return result

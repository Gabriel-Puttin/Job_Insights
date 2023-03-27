from src.pre_built.sorting import sort_by
import pytest

jobs_mock = [
    {
        "title": "Front End Developer",
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "2023-03-26",
    },
    {
        "title": "Back End Developer",
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "2023-03-25",
    },
]


@pytest.fixture
def jobs():
    return jobs_mock


def test_sort_by_criteria(jobs):
    "If sort_by returns correct value"
    sort_by(jobs, "min_salary")
    assert jobs[0]['title'] == 'Back End Developer'

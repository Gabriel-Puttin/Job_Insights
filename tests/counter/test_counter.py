from src.pre_built.counter import count_ocurrences

path = 'data/jobs.csv'


def test_counter():
    'If "count_ocurrences" return the correct value'
    assert count_ocurrences(path, 'Javascript') == 122

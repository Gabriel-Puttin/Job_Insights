from src.pre_built.brazilian_jobs import read_brazilian_file

path = 'tests/mocks/brazilians_jobs.csv'
english_jobs = read_brazilian_file(path)


def test_brazilian_jobs():
    'If brazilian_jobs returns correct value'
    assert read_brazilian_file(path) == english_jobs

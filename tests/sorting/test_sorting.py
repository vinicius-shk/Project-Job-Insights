from src.pre_built.sorting import sort_by
from src.insights.jobs import read


def test_sort_by_criteria():
    file = read("tests/mocks/sort_job_data.csv")
    treated = [
        dic
        for dic in file
        if isinstance(dic["min_salary"], str) is True
        if isinstance(dic["max_salary"], str) is True
        if dic["min_salary"].isnumeric()
        if dic["max_salary"].isnumeric()
        if len(dic["min_salary"]) > 0
        if len(dic["max_salary"]) > 0
    ]
    sort_by(treated, "max_salary")
    assert int(treated[0]["max_salary"]) == 8000
    assert int(treated[-1]["max_salary"]) == 3000
    sort_by(treated, "min_salary")
    assert int(treated[0]["min_salary"]) == 100
    assert int(treated[-1]["min_salary"]) == 4000

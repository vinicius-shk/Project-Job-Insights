from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    file = [
        {"title": "Web developer", "min_salary": "100", "max_salary": "5000"},
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "6000",
        },
        {
            "title": "Back end developer",
            "min_salary": "1050",
            "max_salary": "3000",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {"title": "Eu sou uma batata", "min_salary": "", "max_salary": "8000"},
        {
            "title": "Eu sou uma polenta",
            "min_salary": "10000",
            "max_salary": "",
        },
        {
            "title": "Eu sou uma geleia",
            "min_salary": "'invalid'",
            "max_salary": "1000",
        },
        {
            "title": "Eu sou uma goiaba",
            "min_salary": "1000",
            "max_salary": "'invalid'",
        },
        {
            "title": "Eu sou uma banana",
            "min_salary": "1000",
            "max_salary": "''",
        },
    ]

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

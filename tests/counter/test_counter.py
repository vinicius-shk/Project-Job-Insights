from src.pre_built.counter import count_ocurrences


def test_counter():
    js_counter = count_ocurrences('tests/mocks/jobs.csv', r'front')
    py_counter = count_ocurrences('tests/mocks/jobs.csv', r'full')
    assert js_counter == 1
    assert py_counter == 3

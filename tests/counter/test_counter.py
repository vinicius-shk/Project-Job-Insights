from src.pre_built.counter import count_ocurrences


def test_counter():
    js_counter = count_ocurrences('data/jobs.csv', r'/javascript/')
    py_counter = count_ocurrences('data/jobs.csv', r'/python/')
    assert js_counter > 0
    assert py_counter > 0

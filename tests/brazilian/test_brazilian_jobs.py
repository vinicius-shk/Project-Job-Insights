from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    expected = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert "title" in expected[0]
    assert "titulo" not in expected[0]
    assert "salary" in expected[0]
    assert "salario" not in expected[0]
    assert "type" in expected[0]
    assert "tipo" not in expected[0]

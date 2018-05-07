PARAMS = {
    "test_something": {
        "p1": [1, 2, 3, 4, "bla", ],  # 5
        "p2": [4, 7, 2, ],            # 3 -> 15 test instances
    },
}


def pytest_generate_tests(metafunc):
    def mark_xfails(values):
        # mark test as xfail if one parmeter is a string
        for v in values:
            if isinstance(v, str):
                yield v
                # yield pytest.param(v, marks=[pytest.mark.xfail(reason="can not add str to int", run=False)])
            else:
                yield v

    # check, if a parameter is available for the current test function
    test_function_name = metafunc.function.__name__
    if test_function_name in metafunc.config.my_external_params:
        params = metafunc.config.my_external_params.get(test_function_name)

        # apply the parametrisation if a fixture with the same name as a parameter exists
        for fixture_name, values in params.items():
            if fixture_name in metafunc.fixturenames:
                metafunc.parametrize(fixture_name, mark_xfails(values))


def add(p1, p2):
    return p1 + p2


def test_something(p1, p2):
    assert p1 + p2 == add(p1, p2)
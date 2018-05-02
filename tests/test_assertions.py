from collections import namedtuple

Foo = namedtuple('Foo', ['a', 'b', 'c'])
Foo.__new__.__defaults__ = (None, None, False)


def test_assertion_pass():
    assert True

def test_assertion_set():
    """
    This demonstrates the assertion introspection of python sets
    """
    assert {1, 2, 3} == {2, 3, 4}

def test_assertion_dict():
    """
    This demonstrates the assertion introspection of python dicts
    """
    assert {"a":1, "b": 2} == {"a": 2, "c": 3}

def test_assertion_namedtuple():
    """
    This demonstrates the assertion introspection of collections.namedtuple
    """
    foo1 = Foo("a", "b", False)
    foo2 = Foo("a", 1, False)
    assert foo1 == foo2
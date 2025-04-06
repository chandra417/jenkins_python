import pytest

@pytest.fixture(params=[(1,2), (2,3), (3,4), (4,5)])
def add(request):
    return request.param

def addition(a,b):
    return a  + b

def test_addition(add):
    assert int(add[0]) + int(add[1]) == addition(int(add[0]), int(add[1]))


def test_api_v1():
    from silly_walking.api_v1 import APIv1
    assert APIv1.api_version == 'v1'

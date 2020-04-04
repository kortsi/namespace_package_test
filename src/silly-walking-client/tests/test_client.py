
def test_client():
    from silly_walking.client import Client
    assert Client.api.api_version == 'v1'

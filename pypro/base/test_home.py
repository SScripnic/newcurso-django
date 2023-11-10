from django.test import Client


# Create your tests here.
def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200

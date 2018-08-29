import falcon
from falcon import testing
import json
import pytest

from look.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)

def test_list_images(client):
    doc = {
        'images': [
            {
                'href': 'images/bla.png'
            }
        ]
    }

    response = client.simulate_get('/images')
    result_doc = json.loads(response.content, encoding='utg-8')

    assert result_doc == doc
    assert response.status == falcon.HTTP_200





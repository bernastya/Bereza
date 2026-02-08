import requests

base_url = "https://ru.yougile.com"

my_headers = {
        "Authorization": "Bearer key",
        "Content-Type": "application/json"
    }


def test_add_project():
    project_add = {
        "title": "Новый проект",
    }

    url = f"{base_url}/api-v2/projects"
    resp = requests.post(url, headers=my_headers, json=project_add)
    assert resp.status_code == 201
    response_body = resp.json()
    assert "id" in response_body

import requests

base_url = "https://ru.yougile.com"

my_headers = {
        "Authorization": "Bearer KEY",
        "Content-Type": "application/json"
    }


def test_update_project():
    project_id = ""
    update = {
        "title": "Проект",
    }

    url = f"{base_url}/api-v2/projects/{project_id}"
    resp = requests.put(url, headers=my_headers, json=update)
    assert resp.status_code == 200
    response_body = resp.json()
    assert "id" in response_body
    assert response_body["id"] == project_id

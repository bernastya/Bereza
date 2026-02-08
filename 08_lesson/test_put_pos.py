import requests

base_url = "https://ru.yougile.com"

my_headers = {
        "Authorization": "Bearer key",
        "Content-Type": "application/json"
    }


def test_update_project():
    project_id = "326081e7-f6ce-418f-bf8b-4aa403dcaf0c"
    update = {
        "title": "Проект",
    }
    url = f"{base_url}/api-v2/projects/{project_id}"
    resp = requests.put(url, headers=my_headers, json=update)
    assert resp.status_code == 200
    response_body = resp.json()
    assert "id" in response_body
    assert response_body["id"] == project_id

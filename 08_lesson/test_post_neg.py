import requests

base_url = "https://ru.yougile.com"

my_headers = {
        "Authorization": "Bearer key",
        "Content-Type": "application/json"
    }


def test_edit_project():
    project_edit = {
         "users": {
              "0c549b4e-de0f-4006-a26f-d47e9e74e75a": "admin"
         }
    }

    url = f"{base_url}//api-v2/projects/{{ID_Projekt}}"
    resp = requests.put(url, headers=my_headers, json=project_edit)
    assert resp.status_code == 201
    response_body = resp.json()
    assert "id" in response_body

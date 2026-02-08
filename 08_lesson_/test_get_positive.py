import requests

base_url = "https://ru.yougile.com"

my_headers = {
        "Authorization": "Bearer key",
        "Content-Type": "application/json"
    }


def test_simple_reg():
    resp = requests.get(base_url+'/api-v2/projects', headers=my_headers)
    assert resp.status_code == 200, f"Ошибка {resp.status_code}: {resp.text}"


def test_projekt_id():
    projekt_id = "b090f6d0-037a-4540-b190-7306dd2b5301"
    project_url = f"{base_url}/api-v2/projects/{projekt_id}"
    resp = requests.get(project_url, headers=my_headers)
    assert resp.status_code == 200
    project_data = resp.json()
    assert project_data["id"] == projekt_id

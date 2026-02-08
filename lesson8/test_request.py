import requests


def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')

    response_body = resp.json()
    first_company = response_body[0]

    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
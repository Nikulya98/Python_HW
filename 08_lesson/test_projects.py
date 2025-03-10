import requests

BASE_URL = "https://yougile.com/api-v2/projects"
HEADERS = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}


def test_create_project():
    payload = {
        "title": "Jamaica"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_update_project():
    project_id = "001e5a93-1fa4-406d-8e3b-c523178d0b94"
    payload = {
        "title": "Updated Jamaica"
    }
    response = requests.put(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS,
        json=payload
    )
    print(f"Error: {response.status_code} - {response.text}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id


def test_get_project():
    project_id = "001e5a93-1fa4-406d-8e3b-c523178d0b94"
    response = requests.get(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert "title" in data
    assert "timestamp" in data


def test_create_project_invalid_data():
    response = requests.post(BASE_URL, headers=HEADERS, json={})
    assert response.status_code == 400


def test_update_project_invalid_id():
    project_id = "invalid_id"
    payload = {
        "title": "Updated Jamaica"
    }
    response = requests.put(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS,
        json=payload
    )
    assert response.status_code == 404


def test_get_project_invalid_id():
    project_id = "invalid_id"
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 404

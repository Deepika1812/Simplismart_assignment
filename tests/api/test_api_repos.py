import requests

GITHUB_API_URL = "https://api.github.com"
TOKEN = "your_github_token"

def test_create_repository():
    headers = {"Authorization": f"token {TOKEN}"}
    payload = {"name": "api-test-repo", "private": False}
    response = requests.post(f"{GITHUB_API_URL}/user/repos", json=payload, headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == "api-test-repo"

import requests

GITHUB_API_URL = "https://api.github.com"
OWNER = "your_username"
REPO = "your_repo"
TOKEN = "your_github_token"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def test_create_pull_request():
    url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/pulls"
    payload = {
        "title": "Automated test pull request",
        "head": "feature-branch",  # replace with an existing branch name
        "base": "main",  # replace with your base branch, usually 'main' or 'master'
        "body": "This PR was created via automated API test."
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 201, f"Pull request creation failed: {response.text}"
    data = response.json()
    assert data["title"] == payload["title"]
    print(f"Pull request created: #{data['number']} - {data['title']}")

def test_list_pull_requests():
    url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/pulls"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200, f"Failed to list pull requests: {response.text}"
    pulls = response.json()
    assert isinstance(pulls, list), "Expected pull requests list"
    print(f"Total pull requests fetched: {len(pulls)}")
    for pr in pulls:
        print(f"- #{pr['number']}: {pr['title']} (state: {pr['state']})")

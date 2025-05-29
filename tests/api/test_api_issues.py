import requests

GITHUB_API_URL = "https://api.github.com"
OWNER = "your_username"
REPO = "your_repo"
TOKEN = "your_github_token"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def test_create_issue():
    url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/issues"
    payload = {
        "title": "Automated test issue",
        "body": "This issue was created via automated API test."
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 201, f"Issue creation failed: {response.text}"
    data = response.json()
    assert data["title"] == payload["title"]
    print(f"Issue created: #{data['number']} - {data['title']}")

def test_list_issues():
    url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/issues"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200, f"Failed to list issues: {response.text}"
    issues = response.json()
    assert isinstance(issues, list), "Expected issues list"
    print(f"Total issues fetched: {len(issues)}")
    for issue in issues:
        print(f"- #{issue['number']}: {issue['title']}")

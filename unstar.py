import os
import json
import pathlib
import requests

# personal access token
token = os.environ.get("personal_access_token")

# API endpoint for starred repositories
url = "https://api.github.com/user/starred"
# Set up authentication headers
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28",
}


# Function to fetch starred repositories
def get_starred_repos():
    page = 1
    starred_repos = []
    while True:
        params = {"page": page, "per_page": 100}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            if not data:
                break
            starred_repos.extend(data)
            page += 1
        else:
            print("Failed to fetch starred repositories.")
            break

    return starred_repos


# Function to unstar a repository
def unstar_repo(repo_full_name):
    unstar_url = f"https://api.github.com/user/starred/{repo_full_name}"
    response = requests.delete(unstar_url, headers=headers)
    if response.status_code == 204:
        print(f"Unstarred: {repo_full_name}")
    else:
        print(f"Failed to unstar: {repo_full_name}")


if __name__ == "__main__":
    # Check if starred_repos.json exists, if not fetch starred repositories
    if pathlib.Path("starred_repos.json").exists():
        with open("starred_repos.json", "r") as file:
            starred_repos = json.load(file)
    else:
        starred_repos = get_starred_repos()
        with open("starred_repos.json", "w") as file:
            json.dump(starred_repos, file, indent=4)

    # Unstar all starred repositories
    for repo in starred_repos:
        unstar_repo(repo["full_name"])

    print("Unstarring process completed.")

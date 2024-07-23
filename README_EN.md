# GitHub Star Manager

This Python script allows you to manage your starred repositories on GitHub. It can fetch all your starred repositories and unstar them in bulk.

## Features

- Fetch all starred repositories from your GitHub account
- Save starred repositories to a JSON file for offline access
- Unstar all repositories in bulk

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- `requests` library installed
- A GitHub personal access token with the `user` scope

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/huhusmang/github-star-manager.git
   cd github-star-manager
   ```

2. Install the required Python package:
   ```
   pip install requests
   ```

3. Set up your GitHub personal access token as an environment variable:
   ```
   export personal_access_token=your_token_here
   ```

## Usage

Run the script with Python:

```
python star_manager.py
```

The script will perform the following actions:

1. Check if a `starred_repos.json` file exists:
   - If it exists, load the starred repositories from this file.
   - If it doesn't exist, fetch all starred repositories from GitHub and save them to `starred_repos.json`.

2. Unstar all repositories in the list.

## How It Works

1. The script uses the GitHub API to fetch all starred repositories for the authenticated user.
2. It saves the fetched data to a JSON file for future use and to avoid unnecessary API calls.
3. It then iterates through the list of starred repositories and unstars each one.

## Configuration

The script uses the following GitHub API endpoints:

- `https://api.github.com/user/starred` to fetch starred repositories
- `https://api.github.com/user/starred/{owner}/{repo}` to unstar a specific repository

The GitHub API version used is `2022-11-28`.

## Security

This script requires a GitHub personal access token. Never share your token or commit it to version control. Always use environment variables or secure secret management tools to handle sensitive information.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/huhusmang/github-star-manager/issues) if you want to contribute.
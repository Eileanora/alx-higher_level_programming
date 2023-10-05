#!/usr/bin/python3
'''script that prints the recent 10 commits of a repository by user'''
import requests
from sys import argv


if __name__ == "__main__":
    repository = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner, repository)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))

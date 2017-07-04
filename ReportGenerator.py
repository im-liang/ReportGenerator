from github import Github
import datetime

username = raw_input("Enter your username: ")

password = raw_input("Enter your password: ")

repo = raw_input("Enter your repo: ")

branch = raw_input("Enter your branch: ")

user = Github(username, password).get_user()

repo = user.get_repo(repo)

#get_commits(sha=NotSet, path=NotSet, since=NotSet, until=NotSet, author=NotSet)
commits = repo.get_commits(sha = branch, since = datetime.datetime.now() - datetime.timedelta(days = 7), until = datetime.datetime.now())

for cm in commits:
    print(cm.commit.message)

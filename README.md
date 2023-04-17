# ghunner

ghunner lets you search through both active and completed deployments and runners using 
the GitHub API.

This can be helpful, when automation is used and other workflows triggers a new deployment.
This can help the workflow that triggered the new deployment to wait and see if it was succesful.

# Usage

```bash
ghunner --help
```

Gives you a list of commands e.g. login and runner.


## Login

To be able to login and proive the github token. 

```bash
ghunner login --help
```

Shows that a github token is needed.
```bash
Usage: ghunner login [OPTIONS]

Options:
  --token TEXT  github token e.g. ghp token  [required]
  --help        Show this message and exit.
```

Add token to keyring:
```
ghunner login --token GITHUB_TOKEN
```


## Get deployments

Get the options for all_deployments
```bash
ghunner runner get all_deployments
```

Find deployments:
```bash
ghunner runner get all_deployments --owner owner --repository myproject --tag v1.0.0
```

The output should be something like, but instead of TAG_NAME v1.0.0 etc.
```json
{
  "deployments": [
    {
      "url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME/deployments/869765653",
      "id": 869765653,
      "node_id": "DE_kwDOI7y3-c4z15IV",
      "task": "deploy",
      "original_environment": "all",
      "environment": "all",
      "description": null,
      "created_at": "2023-04-15T16:31:35Z",
      "updated_at": "2023-04-16T06:25:59Z",
      "statuses_url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME/deployments/869765653/statuses",
      "repository_url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME",
      "creator": {
        "login": "LOGIN_NAME[bot]",
        "id": 80842546,
        "node_id": "MDM6Qm90ODA4NDI1NDY=",
        "avatar_url": "https://avatars.githubusercontent.com/in/105625?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D",
        "html_url": "https://github.com/apps/LOGIN_NAME",
        "followers_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/received_events",
        "type": "Bot",
        "site_admin": false
      },
      "sha": "b436d0b6d701102e67392233ff368a9a9fa170c8",
      "ref": "TAG_NAME",
      "payload": {},
      "transient_environment": false,
      "production_environment": false,
      "performed_via_github_app": null
    },
    {
      "url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME/deployments/869763720",
      "id": 869763720,
      "node_id": "DE_kwDOI7y3-c4z14qI",
      "task": "deploy",
      "original_environment": "all",
      "environment": "all",
      "description": null,
      "created_at": "2023-04-15T16:27:40Z",
      "updated_at": "2023-04-15T16:32:48Z",
      "statuses_url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME/deployments/869763720/statuses",
      "repository_url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME",
      "creator": {
        "login": "LOGIN_NAME[bot]",
        "id": 80842546,
        "node_id": "MDM6Qm90ODA4NDI1NDY=",
        "avatar_url": "https://avatars.githubusercontent.com/in/105625?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D",
        "html_url": "https://github.com/apps/LOGIN_NAME",
        "followers_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/received_events",
        "type": "Bot",
        "site_admin": false
      },
      "sha": "b436d0b6d701102e67392233ff368a9a9fa170c8",
      "ref": "TAG_NAME",
      "payload": {},
      "transient_environment": false,
      "production_environment": false,
      "performed_via_github_app": null
    }
  ],
  "statuses": {
    "869765653": "success",
    "869763720": "success"
  },
  "all_completed": true,
  "all_success": true
}
{
  "deployments": [
    {
      "url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME/deployments/869765653",
      "id": 869765653,
      "node_id": "DE_kwDOI7y3-c4z15IV",
      "task": "deploy",
      "original_environment": "all",
      "environment": "all",
      "description": null,
      "created_at": "2023-04-15T16:31:35Z",
      "updated_at": "2023-04-16T06:25:59Z",
      "statuses_url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME/deployments/869765653/statuses",
      "repository_url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME",
      "creator": {
        "login": "LOGIN_NAME[bot]",
        "id": 80842546,
        "node_id": "MDM6Qm90ODA4NDI1NDY=",
        "avatar_url": "https://avatars.githubusercontent.com/in/105625?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D",
        "html_url": "https://github.com/apps/APP_NAME",
        "followers_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/received_events",
        "type": "Bot",
        "site_admin": false
      },
      "sha": "b436d0b6d701102e67392233ff368a9a9fa170c8",
      "ref": "TAG_NAME",
      "payload": {},
      "transient_environment": false,
      "production_environment": false,
      "performed_via_github_app": null
    },
    {
      "url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME/deployments/869763720",
      "id": 869763720,
      "node_id": "DE_kwDOI7y3-c4z14qI",
      "task": "deploy",
      "original_environment": "all",
      "environment": "all",
      "description": null,
      "created_at": "2023-04-15T16:27:40Z",
      "updated_at": "2023-04-15T16:32:48Z",
      "statuses_url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME/deployments/869763720/statuses",
      "repository_url": "https://api.github.com/repos/REPOSITORY_OWNER/REPOSITORY_NAME",
      "creator": {
        "login": "LOGIN_NAME[bot]",
        "id": 80842546,
        "node_id": "MDM6Qm90ODA4NDI1NDY=",
        "avatar_url": "https://avatars.githubusercontent.com/in/105625?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D",
        "html_url": "https://github.com/apps/LOGIN_NAME",
        "followers_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/LOGIN_NAME%5Bbot%5D/received_events",
        "type": "Bot",
        "site_admin": false
      },
      "sha": "b436d0b6d701102e67392233ff368a9a9fa170c8",
      "ref": "TAG_NAME",
      "payload": {},
      "transient_environment": false,
      "production_environment": false,
      "performed_via_github_app": null
    }
  ],
  "statuses": {
    "869765653": "success",
    "869763720": "success"
  },
  "all_completed": true,
  "all_success": true
}

```

## Get Runners

get options for running:
```bash
ghunner runner get all_runners --help
```

Run program to fetch every runner from a date with status `success` or `failure`.
```bash
ghunner runner get all_runners --owner OWNER --repository REPOSITORY_NAME --created_at_from '2023-04-10 01:01:01' --status success --status failure
```

The expected output should be something like:
```json
{
  "workflow_runs": [
    {
      "id": 4718147291,
      "name": "Deploy Code to K8s - Production",
      "node_id": "WFR_kwLOI7y3-c8AAAABGTk22w",
      "head_branch": "TAG",
      "head_sha": "99721644b57eb45a04867431d97aa9ebd8b4b9d5",
      "path": ".github/workflows/prod-deployment.yml",
      "display_title": "commit message",
      "run_number": 49,
      "event": "push",
      "status": "completed",
      "conclusion": "success",
      "workflow_id": 47902028,
      "check_suite_id": 12276514829,
      "check_suite_node_id": "CS_kwDOI7y3-c8AAAAC27zADQ",
      "url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/actions/runs/4718147291",
      "html_url": "https://github.com/OWNER/REPOSITORY_NAME/actions/runs/4718147291",
      "pull_requests": [],
      "created_at": "2023-04-17T06:26:40Z",
      "updated_at": "2023-04-17T06:31:31Z",
      "actor": {
        "login": "GITHUB_USER",
        "id": 128375254,
        "node_id": "U_kgDOB6bZ1g",
        "avatar_url": "https://avatars.githubusercontent.com/u/128375254?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/GITHUB_USER",
        "html_url": "https://github.com/GITHUB_USER",
        "followers_url": "https://api.github.com/users/GITHUB_USER/followers",
        "following_url": "https://api.github.com/users/GITHUB_USER/following{/other_user}",
        "gists_url": "https://api.github.com/users/GITHUB_USER/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/GITHUB_USER/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/GITHUB_USER/subscriptions",
        "organizations_url": "https://api.github.com/users/GITHUB_USER/orgs",
        "repos_url": "https://api.github.com/users/GITHUB_USER/repos",
        "events_url": "https://api.github.com/users/GITHUB_USER/events{/privacy}",
        "received_events_url": "https://api.github.com/users/GITHUB_USER/received_events",
        "type": "User",
        "site_admin": false
      },
      "run_attempt": 1,
      "referenced_workflows": [
        {
          "path": "OWNER/folder/.github/workflows/model-deployment.yml@main",
          "sha": "dc363a0c485ac31c6a371be45f556481e1ae2f40",
          "ref": "refs/heads/main"
        },
        {
          "path": "OWNER/folder/.github/workflows/container-ready.yml@dc363a0c485ac31c6a371be45f556481e1ae2f40",
          "sha": "dc363a0c485ac31c6a371be45f556481e1ae2f40",
          "ref": "refs/heads/main"
        }
      ],
      "run_started_at": "2023-04-17T06:26:40Z",
      "triggering_actor": {
        "login": "GITHUB_USER",
        "id": 128375254,
        "node_id": "U_kgDOB6bZ1g",
        "avatar_url": "https://avatars.githubusercontent.com/u/128375254?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/GITHUB_USER",
        "html_url": "https://github.com/GITHUB_USER",
        "followers_url": "https://api.github.com/users/GITHUB_USER/followers",
        "following_url": "https://api.github.com/users/GITHUB_USER/following{/other_user}",
        "gists_url": "https://api.github.com/users/GITHUB_USER/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/GITHUB_USER/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/GITHUB_USER/subscriptions",
        "organizations_url": "https://api.github.com/users/GITHUB_USER/orgs",
        "repos_url": "https://api.github.com/users/GITHUB_USER/repos",
        "events_url": "https://api.github.com/users/GITHUB_USER/events{/privacy}",
        "received_events_url": "https://api.github.com/users/GITHUB_USER/received_events",
        "type": "User",
        "site_admin": false
      },
      "jobs_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/actions/runs/4718147291/jobs",
      "logs_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/actions/runs/4718147291/logs",
      "check_suite_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/check-suites/12276514829",
      "artifacts_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/actions/runs/4718147291/artifacts",
      "cancel_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/actions/runs/4718147291/cancel",
      "rerun_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/actions/runs/4718147291/rerun",
      "previous_attempt_url": null,
      "workflow_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/actions/workflows/47902028",
      "head_commit": {
        "id": "99721644b57eb45a04867431d97aa9ebd8b4b9d5",
        "tree_id": "d7295c8bf88e0e90a3849f57b4034eed6fb3e8f7",
        "message": "commit message",
        "timestamp": "2023-04-17T06:26:17Z",
        "author": {
          "name": "GITHUB_USER",
          "email": "name@business.dk"
        },
        "committer": {
          "name": "GITHUB_USER",
          "email": "name@business.dk"
        }
      },
      "repository": {
        "id": 599570425,
        "node_id": "R_kgDOI7y3-Q",
        "name": "REPOSITORY_NAME",
        "full_name": "OWNER/REPOSITORY_NAME",
        "private": true,
        "owner": {
          "login": "OWNER",
          "id": 79060207,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjc5MDYwMjA3",
          "avatar_url": "https://avatars.githubusercontent.com/u/79060207?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/OWNER",
          "html_url": "https://github.com/OWNER",
          "followers_url": "https://api.github.com/users/OWNER/followers",
          "following_url": "https://api.github.com/users/OWNER/following{/other_user}",
          "gists_url": "https://api.github.com/users/OWNER/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/OWNER/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/OWNER/subscriptions",
          "organizations_url": "https://api.github.com/users/OWNER/orgs",
          "repos_url": "https://api.github.com/users/OWNER/repos",
          "events_url": "https://api.github.com/users/OWNER/events{/privacy}",
          "received_events_url": "https://api.github.com/users/OWNER/received_events",
          "type": "Organization",
          "site_admin": false
        },
        "html_url": "https://github.com/OWNER/REPOSITORY_NAME",
        "description": "Template Project",
        "fork": false,
        "url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME",
        "forks_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/forks",
        "keys_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/teams",
        "hooks_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/hooks",
        "issue_events_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/issues/events{/number}",
        "events_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/events",
        "assignees_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/assignees{/user}",
        "branches_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/branches{/branch}",
        "tags_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/tags",
        "blobs_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/languages",
        "stargazers_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/stargazers",
        "contributors_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/contributors",
        "subscribers_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/subscribers",
        "subscription_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/subscription",
        "commits_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/contents/{+path}",
        "compare_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/merges",
        "archive_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/downloads",
        "issues_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/issues{/number}",
        "pulls_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/labels{/name}",
        "releases_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/releases{/id}",
        "deployments_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/deployments"
      },
      "head_repository": {
        "id": 599570425,
        "node_id": "R_kgDOI7y3-Q",
        "name": "REPOSITORY_NAME",
        "full_name": "OWNER/REPOSITORY_NAME",
        "private": true,
        "owner": {
          "login": "OWNER",
          "id": 79060207,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjc5MDYwMjA3",
          "avatar_url": "https://avatars.githubusercontent.com/u/79060207?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/OWNER",
          "html_url": "https://github.com/OWNER",
          "followers_url": "https://api.github.com/users/OWNER/followers",
          "following_url": "https://api.github.com/users/OWNER/following{/other_user}",
          "gists_url": "https://api.github.com/users/OWNER/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/OWNER/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/OWNER/subscriptions",
          "organizations_url": "https://api.github.com/users/OWNER/orgs",
          "repos_url": "https://api.github.com/users/OWNER/repos",
          "events_url": "https://api.github.com/users/OWNER/events{/privacy}",
          "received_events_url": "https://api.github.com/users/OWNER/received_events",
          "type": "Organization",
          "site_admin": false
        },
        "html_url": "https://github.com/OWNER/REPOSITORY_NAME",
        "description": "Template Project",
        "fork": false,
        "url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME",
        "forks_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/forks",
        "keys_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/teams",
        "hooks_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/hooks",
        "issue_events_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/issues/events{/number}",
        "events_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/events",
        "assignees_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/assignees{/user}",
        "branches_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/branches{/branch}",
        "tags_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/tags",
        "blobs_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/languages",
        "stargazers_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/stargazers",
        "contributors_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/contributors",
        "subscribers_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/subscribers",
        "subscription_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/subscription",
        "commits_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/contents/{+path}",
        "compare_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/merges",
        "archive_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/downloads",
        "issues_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/issues{/number}",
        "pulls_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/labels{/name}",
        "releases_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/releases{/id}",
        "deployments_url": "https://api.github.com/repos/OWNER/REPOSITORY_NAME/deployments"
      }
    },
    ......
  ],
  "statuses": [
    "completed",
    .......
  ],
  "conclusions": [
    "success",
    .......
  ],
  "all_completed": true,
  "all_success": false
}


```




# Ubuntu Workflow 

ghunner uses the python library Keyring to save the token outside of the script. To 
be able to use this in a github workflow, it needs to be enabled.

install and unlock gnome keyring:
```bash
sudo apt-get install -y dbus dbus-x11 gnome-keyring
gnome-keyring-daemon --unlock
```

https://github.com/actions/runner-images/issues/6683

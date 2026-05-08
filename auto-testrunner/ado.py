import base64

import requests

from config import DEVOPS_ACCESS_TOKEN, DEVOPS_ORG, DEVOPS_PROJECT, DEVOPS_REPO


def ado_headers():
    token = base64.b64encode(f":{DEVOPS_ACCESS_TOKEN}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def fetch_open_prs():
    url = (
        f"https://dev.azure.com/{DEVOPS_ORG}/{DEVOPS_PROJECT}"
        f"/_apis/git/repositories/{DEVOPS_REPO}/pullrequests"
        f"?searchCriteria.status=active&searchCriteria.targetRefName=refs/heads/15.0-dev&api-version=7.0"
    )
    resp = requests.get(url, headers=ado_headers(), timeout=30)
    resp.raise_for_status()
    return resp.json().get("value", [])


def fetch_pr_details(pr_id):
    """Returns {"head": commit_id, "status": "active"|"abandoned"|"completed"}."""
    url = (
        f"https://dev.azure.com/{DEVOPS_ORG}/{DEVOPS_PROJECT}"
        f"/_apis/git/repositories/{DEVOPS_REPO}/pullrequests/{pr_id}"
        f"?api-version=7.0"
    )
    resp = requests.get(url, headers=ado_headers(), timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return {
        "head": data.get("lastMergeSourceCommit", {}).get("commitId"),
        "status": data.get("status", "unknown"),
    }


def comment_exists_for_commit(pr_id, commit_hash):
    url = (
        f"https://dev.azure.com/{DEVOPS_ORG}/{DEVOPS_PROJECT}"
        f"/_apis/git/repositories/{DEVOPS_REPO}/pullrequests/{pr_id}/threads"
        f"?api-version=7.0"
    )
    resp = requests.get(url, headers=ado_headers(), timeout=30)
    resp.raise_for_status()
    marker = f"[HEAD {commit_hash[:8]}]"
    for thread in resp.json().get("value", []):
        for comment in thread.get("comments", []):
            if marker in (comment.get("content") or ""):
                return True
    return False


def upload_pr_attachment(pr_id, filename, file_path):
    url = (
        f"https://dev.azure.com/{DEVOPS_ORG}/{DEVOPS_PROJECT}"
        f"/_apis/git/repositories/{DEVOPS_REPO}/pullrequests/{pr_id}"
        f"/attachments/{filename}?api-version=7.1"
    )
    headers = {**ado_headers(), "Content-Type": "application/octet-stream"}
    with open(file_path, "rb") as f:
        resp = requests.post(url, data=f, headers=headers, timeout=60)
    resp.raise_for_status()
    return resp.json().get("url")


def post_pr_comment(pr_id, content):
    url = (
        f"https://dev.azure.com/{DEVOPS_ORG}/{DEVOPS_PROJECT}"
        f"/_apis/git/repositories/{DEVOPS_REPO}/pullrequests/{pr_id}"
        f"/threads?api-version=7.0"
    )
    body = {"comments": [{"content": content, "commentType": 1}], "status": 1}
    resp = requests.post(url, json=body, headers=ado_headers(), timeout=30)
    resp.raise_for_status()

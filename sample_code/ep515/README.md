# [make a github commit using only the api! (intermediate)](https://youtu.be/nwHqXtk6LHA)

Today I show of a task which I've done a few times and my learnings about it -- how to make a git commit using the api!

## Interactive examples

### Bash

```bash
GH_CURL=(curl -H "Authorization: token $GH_TOKEN")

"${GH_CURL[@]}" --silent https://api.github.com/repos/asottile/astpretty | jq .
"${GH_CURL[@]}" --silent https://api.github.com/repos/asottile/astpretty | jq .default_branch

"${GH_CURL[@]}" --silent https://api.github.com/repos/asottile/astpretty/branches/<branch_name> | jq .
"${GH_CURL[@]}" --silent https://api.github.com/repos/asottile/astpretty/branches/<branch_name> | jq . | grep sha

"${GH_CURL[@]}" --silent https://api.github.com/repos/asottile/astpretty/branches/<branch_name> | jq .commit
"${GH_CURL[@]}" --silent https://api.github.com/repos/asottile/astpretty/branches/<branch_name> | jq .commit.sha
"${GH_CURL[@]}" --silent https://api.github.com/repos/asottile/astpretty/branches/<branch_name> | jq .commit.commit.tree.sha

"${GH_CURL[@]}" --silent -XPOST https://api.github.com/repos/asottile/astpretty/git/trees -d '{"base_tree": "<tree_hash>", "tree": [{"path": "README.md", "mode": "100644", "type": "blob", "content": "hello hello world\n"}]}'
"${GH_CURL[@]}" --silent -XPOST https://api.github.com/repos/asottile/astpretty/git/trees -d '{"base_tree": "<tree_hash>", "tree": [{"path": "README.md", "mode": "100644", "type": "blob", "content": "hello hello world\n"}]}' | jq .sha

"${GH_CURL[@]}" --silent -XPOST https://api.github.com/repos/asottile/astpretty/git/commits -d '{"message": "hello hello world", "tree": "<tree_hash>", "parents": ["commit_hash"]}'
"${GH_CURL[@]}" --silent -XPOST https://api.github.com/repos/asottile/astpretty/git/refs -d '{"sha": "<commit_hash>", "ref": "refs/heads/hello-hello-world"}'
```

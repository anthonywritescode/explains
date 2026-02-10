#!/usr/bin/env bash
git-filter-repo --commit-callback '
    if not commit.message.startswith(b"Merge pull request "):
        return commit
    else:
        assert len(commit.parents) == 2, vars(commit)
        del commit.parents[1]
        return commit
'

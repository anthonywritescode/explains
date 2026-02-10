#!/usr/bin/env bash
git-filter-repo --commit-callback '
    if commit.message.startswith(b"Merge pull request ") and len(commit.parents) == 2:
        assert len(commit.parents) == 2, vars(commit)
        del commit.parents[1]
        return commit
    else:
        return commit
'

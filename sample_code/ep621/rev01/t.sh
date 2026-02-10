#!/usr/bin/env bash
set -euxo pipefail

rm -rf jac-vscode-fb

cp -r jaseci-archived jac-vscode-fb

FILTER_BRANCH_SQUELCH_WARNING=1 git -C jac-vscode-fb filter-branch \
    --tree-filter "python3 -S $PWD/rewrite.py" \
    --msg-filter 'sed -r "s|(#[0-9]+)|jaseci-labs/jaseci\1|g"' \
    -- -- \
    support/vscode_ext/jac \
    jaclang/support/vscode_ext/jac \
    jac/support/vscode_ext/jac

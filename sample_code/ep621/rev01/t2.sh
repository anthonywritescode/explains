#!/usr/bin/env bash
set -euxo pipefail

rm -rf jac-vscode-fr

cp -r jaseci-archived jac-vscode-fr

pushd jac-vscode-fr
../venv/bin/git-filter-repo \
    --force \
    --path=support/vscode_ext/jac \
    --path-rename=support/vscode_ext/jac/: \
    --path=jaclang/support/vscode_ext/jac \
    --path-rename=jaclang/support/vscode_ext/jac/: \
    --path=jac/support/vscode_ext/jac \
    --path-rename=jac/support/vscode_ext/jac/: \
    --replace-message <(echo 'regex:#(?=[0-9]+)==>jaseci-labs/jaseci#')
popd

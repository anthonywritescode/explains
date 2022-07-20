#!/usr/bin/env bash
set -euox pipefail

var="$(does-not-exist wat)"
echo "hello hello world $var"

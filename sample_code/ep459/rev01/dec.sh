#!/usr/bin/env bash
set -euo pipefail

base64 -d "$1" |
    openssl pkeyutl -decrypt -inkey ~/.ssh/id_rsa -in /dev/stdin -out /dev/stdout

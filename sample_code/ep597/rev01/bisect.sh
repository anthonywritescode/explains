set -euxo pipefail
git -C ../sentry checkout -q $(cat sentry-version)
pip install -qq -r sentry-requirements-dev-frozen.txt
exec python3 t.py

set -euxo pipefail

rm -rf inner.zip outer.zip packages.json node_modules out-1 out-2

wget -q -O inner.zip https://github.com/getsentry/sentry-android-gradle-plugin/releases/download/4.3.0/sentry-android-gradle-plugin-4.3.0.zip
sha256sum --check <<< 'f20bc17f0459128ad89c6d17947b9e9dd7286eacd686c69beae90f9f9969081c inner.zip'

zip outer.zip inner.zip
npm install unzipper >& /dev/null

node t.mjs outer.zip out-1
sha256sum --check <<< 'f20bc17f0459128ad89c6d17947b9e9dd7286eacd686c69beae90f9f9969081c out-1/inner.zip'

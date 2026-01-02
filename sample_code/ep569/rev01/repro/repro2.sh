rm -rf out-1 out-2

node t.mjs outer.zip out-1 || exit 1
node t.mjs out-1/inner.zip out-2 || exit 1

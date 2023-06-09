FROM bitnami/git
RUN --mount=type=ssh GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git clone git@github.com:asottile/pyupgrade

# Add the following to ~/.bash_profile
# export PYTHONSTARTUP=~/.pythonrc.py
import readline
import rlcompleter  # noqa: F401
readline.parse_and_bind('tab: complete')

type(exit).__repr__ = lambda self: self()

# [debugging and fixing pyuwsgi in python 3.12 (advanced)](https://youtu.be/Y4n2xCIF2Jg)

welcome to a whirlwind tour of bisecting, GIL, strace, gdb, forking, threadstates, undefined behaviour, and deadlocking.  I go through the process debugging the most difficult bug I've encountered yet and ultimately how I fixed the problem and understood what changed and why it resulted in this issue!

## Interactive examples

Session 1:

### Bash

```bash
virtualenv venv -ppython3.12
. venv/bin/activate
pip install pyuwsgi==2.0.26

chmod +x t.sh
bash t.sh
pkill -9 -f uwsgi
fg

cd cpython
git bisect start
git bisect good v3.12.0a2
git bisect bad v3.12.0rc1
git bisect run ../venv-bisect/bin/python3 ../bisect-uwsgi.py

git clone git@github.com:lincolnloop/pyuwsgi-wheels
cd pyuwsgi-wheels/uwsgi/

git grep IsInit
nano plugins/python/python_plugin.c
nano plugins/pyuwsgi/pyuwsgi.c

git grep PyEval_RestoreThread
git grep -n PyEval_RestoreThread

git grep uwsgi_fork
nano core/master_utils.c

./venv.uwsgi/bin/pip uninstall uwsgi
./venv.uwsgi/bin/pip install ./uwsgi

chmod +x t.sh
bash t.sh

git -C ../../uwsgi diff -- core/
git -C ../../uwsgi diff -- core/ | git apply
cd ../../

./venv/bin/pip uninstall pyuwsgi
./venv/bin/pip install ./pyuwsgi-wheels/uwsgi/

nano pyuwsgi-wheels/uwsgi/plugins/pyuwsgi/pyuwsgi.c
```

Session 2:

```bash
yes | head -60 | xargs --replace curl localhost:9001/health-check/; echo
```

Session 3:

```bash
which strace
strace --help

ps -ef | grep uwsgi
sudo strace -p <pid>
sudo gdb -p <pid>

# where
# bt
# q

ps -ef | grep uwsgi
sudo gdb -p <pid>

# b plugins/python/gil.c:12
# c
# p _Py_tss_tstate
# c
# q

sudo gdb -p <pid>

# b plugins/python/gil.c:12
# c
# p_Py_tss_tstate->interp->ceval->gil->locked
# p _Py_tss_tstate
# q

sudo gdb -p <pid>

# b plugins/python/gil.c:12
# c
# p _PyRuntime.ceval.gil->locked
# p _Py_tss_tstate
# q
```

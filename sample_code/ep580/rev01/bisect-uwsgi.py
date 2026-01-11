from __future__ import annotations
import contextlib
import os.path
# import shlex
import subprocess
import urllib.request
import sys
import time
from typing import Generator
# from typing import IO
import psutil


rev = subprocess.check_output(('git', 'rev-parse', 'HEAD'), text=True).strip()

prefix = os.path.abspath('../prefix')
venv = os.path.abspath('../venv')
logs = os.path.abspath('../logs')
uwsgi_src = os.path.abspath('../pyuwsgi-wheels/uwsgi')


def tee() -> None:
    ...


def _cmd_q() -> None:
    ...


def _build_cpython() -> None:
    print('!!! building cpython')
    _cmd_q('git', 'clean', '-fxfd')
    _cmd_q('./configure', '--prefix', prefix)
    _cmd_q('make', '-j5')
    _cmd_q('make', 'install')


def _make_venv() -> None:
    print('!!! making venv')
    _cmd_q('rm', '-rf', venv)
    _cmd_q(os.path.join(prefix, 'bin', 'python3'), '-mvenv', venv)


def _install_uwsgi() -> None:
    print('!!! installing uwsgi')
    _cmd_q(os.path.join(venv, 'bin', 'pip'), 'install', uwsgi_src)


def _req() -> None:
    urllib.request.urlopen('http://127.0.0.1:9001/', timeout=1).read()


def _wait_for_ready() -> None:
    for _ in range(10):
        try:
            _req()
        except OSError:
            print('...waiting for start', file=sys.stderr)
            time.sleep(.25)
        else:
            return


def _child_pids(pid: int) -> tuple[int, ...]:
    return tuple(child.pid for child in psutil.Process(pid).children())


@contextlib.contextmanager
def uwsgi_proc() -> Generator[int]:
    uwsgi = os.path.join(venv, 'bin', 'uwsgi')
    _cmd_q(uwsgi, '--help')
    env = {
        **os.environ,
        'UWSGI_MASTER': 'true',
        'UWSGI_BINARY_PATH': os.path.join(venv, 'bin', 'python3'),
        'UWSGI_VIRTUALENV': venv,
        'UWSGI_WORKERS': '2',
        'UWSGI_ENABLE_THREADS': 'true',
        'UWSGI_MAX_REQUESTS': '2',
        'UWSGI_SINGLE_INTERPRETER': 'true',
        'UWSGI_HTTP_SOCKET': 'localhost:9001',
        'UWSGI_WSGI_FILE': 'wsgi.py',
        'UWSGI_DISABLE_LOGGING': '1',
    }
    with open(os.path.join(logs, rev), 'a+') as logfile:
        tee('+ uwsgi', logfile, sys.stderr)
        proc = subprocess.Popen(
            (uwsgi, ),
            env=env,
            cwd='..',
            stdout=logfile,
            stderr=logfile,
        )
        _wait_for_ready()
        try:
            yield proc.pid
        finally:
            to_kill = [str(proc.pid)]
            for child_pid in _child_pids(proc.pid):
                to_kill.append(str(child_pid))
            subprocess.call(('kill', '-9', *to_kill))


def _run_test() -> int:
    with uwsgi_proc() as pid:
        children = set(_child_pids(pid))
        print(f'started with pid: {pid} {children}!', file=sys.stderr)
        while True:
            time.sleep(.25)
            try:
                _req()
            except OSError:
                cand_children = set(_child_pids(pid))
                assert not children & cand_children, (children, cand_children)
                print('\ngot deadlock!!')
                return 1
            else:
                cand_children = set(_child_pids(pid))
                if cand_children & children:
                    print('z', flush=True, end='')
                    continue
                else:
                    print('\nsuccessful request after all children recycled!')
                    return 0


def main() -> int:
    assert os.path.exists('Python'), 'not in cpython'
    _build_cpython()
    _make_venv()
    _install_uwsgi()
    return _run_test()


if __name__ == '__main__':
    raise SystemExit(main())

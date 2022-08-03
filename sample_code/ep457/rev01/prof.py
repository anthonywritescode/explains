import cProfile
import importlib.metadata
import sys


def main() -> int:
    ep_name = sys.argv.pop(1)
    ep, = {
        ep
        for dist in importlib.metadata.distributions()
        for ep in dist.entry_points
        if ep.group == 'console_scripts' and ep.name == ep_name
    }

    main = ep.load()
    with cProfile.Profile() as p:
        main()
    p.dump_stats('out.pstats')


if __name__ == '__main__':
    raise SystemExit(main())

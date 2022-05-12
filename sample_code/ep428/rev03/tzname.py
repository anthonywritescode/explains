import argparse
import datetime
import sys

if sys.version_info >= (3, 9):
    import zoneinfo
else:
    from backports import zoneinfo


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('date')
    args = parser.parse_args()

    dt = datetime.datetime.strptime(args.date, '%Y-%m-%d')
    dt = dt.replace(tzinfo=zoneinfo.ZoneInfo('America/Detroit'))

    print(dt.tzname())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

from _lru_cache import LRUCache


def main() -> int:
    caches = {}

    with open('lru_cache.log') as f:
        for line in f:
            line = line.replace(': ', ' ')

            match line.split():
                case [cid, '__init__']:
                    caches[cid] = LRUCache(max_size=100)
                case [cid, 'set', k, *v]:
                    caches[cid].set(k, ' '.join(v))
                case [cid, '__copy__', '->', cid2]:
                    caches[cid2] = caches[cid].__copy__()
                case unreachable:
                    raise AssertionError(unreachable)


if __name__ == '__main__':
    raise SystemExit(main())

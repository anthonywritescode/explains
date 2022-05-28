import asyncio


async def f1(x: int) -> None:
    await asyncio.sleep(x / 10)
    print(f'hi from {x}')


async def amain() -> int:
    futures = [f1(i) for i in range(5)]
    await asyncio.gather(*futures)
    print('done')
    return 0


def main() -> int:
    return asyncio.run(amain())


if __name__ == '__main__':
    raise SystemExit(main())

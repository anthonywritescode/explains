import asyncio


async def f1(x: int) -> None:
    await asyncio.sleep(x / 10)
    print(f'hi from {x}')


async def f2():
    raise ValueError(1)


async def f3():
    2 * 3 * (4 * None)


async def amain() -> int:
    # futures = [f1(i) for i in range(5)]
    # await asyncio.gather(*futures)

    try:
        async with asyncio.TaskGroup() as tg:
            for i in range(5):
                tg.create_task(f1(i))
            tg.create_task(f2())
            tg.create_task(f2())
            tg.create_task(f3())
    except* AssertionError as eg:
        print(f'got AE {eg}')
    except* ValueError as eg:
        print(f'got VE {eg}')

    print('done')
    return 0


def main() -> int:
    return asyncio.run(amain())


if __name__ == '__main__':
    raise SystemExit(main())

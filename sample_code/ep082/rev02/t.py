from typing import Type


def catch_these(tp: Type[BaseException]) -> None:
    try:
        raise AssertionError('hello')
    except tp as e:
        print(f'caught {tp}: {e}')
    except Exception:
        print(f'not caught: {tp}')


catch_these(TypeError)
catch_these(AssertionError)
catch_these((TypeError, AssertionError))

# except (TypeError, AssertionError) as e:


def get_thing(): ...


def log_thing(e): ...


try:
    # code which may raise an exception
    response = get_thing()
except (TypeError, AssertionError):
    # code that runs when an exception occurs
    ...
except Exception as e:
    # code that runs when an exception occurs
    log_thing(e)
    raise
except BaseException:
    # code that runs when an exception occurs
    ...
else:
    # code that only runs if successful
    data = response.json()
    data['foo'] = 'bar'
finally:
    # always runs independent of success
    ...

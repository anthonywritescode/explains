

try:
    # code which may raise an exception
    ...
except (TypeError, AssertionError):
    # code that runs when an exception occurs
    ...
except Exception as e:
    # code that runs when an exception occurs
    ...
except BaseException:
    # code that runs when an exception occurs
    ...
else:
    # code that only runs if successful
    ...
finally:
    # always runs independent of success
    ...

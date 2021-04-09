status_code = 404

HTTP_OK = 200

match status_code:
    case _:
        print(f'status OK {_}')

status_code = 404

HTTP_OK = 200

match status_code:
    case HTTP_OK:
        print(f'status OK {HTTP_OK}')

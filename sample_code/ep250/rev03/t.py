status_code = 404

HTTP_OK = 200

match status_code:
    case HTTP_OK:
        print('status OK')
    case 400:
        print('bad request')
    case 404:
        print('not found')

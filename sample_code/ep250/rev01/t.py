status_code = 404

match status_code:
    case 200:
        print('status OK')
    case 400:
        print('bad request')
    case 404:
        print('not found')
    case 418:
        print('I am a teapot')

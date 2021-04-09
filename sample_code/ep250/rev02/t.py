status_code = 'foo'

match status_code:
    case 'bar':
        print('matched bar')
    case 'foo':
        print('matched foo')
    case 200:
        print('status OK')
    case 400:
        print('bad request')
    case 404:
        print('not found')
    case 418:
        print('I am a teapot')

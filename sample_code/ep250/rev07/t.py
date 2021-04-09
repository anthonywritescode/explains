status_code = 404


class StatusCodes:
    HTTP_OK = 200
    HTTP_BAD_REQUEST = 400
    HTTP_NOT_FOUND = 404


match status_code:
    case StatusCodes.HTTP_OK:
        print('ok')
    case StatusCodes.HTTP_BAD_REQUEST | StatusCodes.HTTP_NOT_FOUND:
        print('got 40x error')
    case StatusCodes.HTTP_NOT_FOUND:
        print('not found')

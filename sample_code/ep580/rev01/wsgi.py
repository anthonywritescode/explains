def application(environ, start_response):
    print('.', end='', flush=True)

    status = '200 OK'
    output = b'!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

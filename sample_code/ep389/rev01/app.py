import flask

app = flask.Flask(__name__)

logged_in = False


def user_or_log_in():
    if logged_in:
        return '<strong> you are logged in!</strong>'
    else:
        return f'<a href="/login?return_url={flask.request.url}">login</a>'


@app.route('/')
def index():
    return f'''\
<!doctype html>
<html>
    <body>
        welcome to home<br>
        {user_or_log_in()}
    </body>
</html>
'''


@app.route('/page1')
def page1():
    return f'''\
<!doctype html>
<html>
    <body>
        welcome to page 1!<br>
        {user_or_log_in()}
    </body>
</html>
'''


@app.route('/login')
def login():
    global logged_in
    logged_in = True
    if 'return_url' in flask.request.args:
        return flask.redirect(flask.request.args['return_url'])
    else:
        return flask.redirect('/')


if __name__ == '__main__':
    app.run()

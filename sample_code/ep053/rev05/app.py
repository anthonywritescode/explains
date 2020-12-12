import flask
from flask_wtf.csrf import CSRFProtect


app = flask.Flask(__name__)
csrf = CSRFProtect(app)


@app.route('/target', methods=['POST'])
def target():
    return 'the missiles were fired'


@app.route('/')
def index():
    return flask.render_template_string('''\
<!doctype html>
<html>
    <body>
        <form action="/target" method="post">
            <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
            <input type="submit" value="fire the missiles">
        </form>
    </body>
</html>
''')


def main():
    app.config.from_pyfile('config.py')
    csrf.init_app(app)
    app.run(port=9002)


if __name__ == '__main__':
    exit(main())

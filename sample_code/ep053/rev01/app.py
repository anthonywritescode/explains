import flask


app = flask.Flask(__name__)


@app.route('/target', methods=['POST'])
def target():
    return 'the missiles were fired'


@app.route('/')
def index():
    return '''\
<!doctype html>
<html>
    <body>
        <form action="/target" method="post">
            <input type="submit" value="fire the missiles">
        </form>
    </body>
</html>
'''


def main():
    app.run(port=9002)


if __name__ == '__main__':
    exit(main())

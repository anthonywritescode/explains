# [web security: what is a csrf exploit? (intermediate)](https://youtu.be/MXZhe0KduyE)

Today I cover a topic which came up on stream recently: what is CSRF / XSRF and why should I care?  I show a demo application which has this problem as well as a real world example that I exploited.

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install Flask Flask-WTF
```

## Interactive examples

### Bash

```bash
python app.py

firefox index.html &
```

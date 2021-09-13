import os


# PORT = int(os.environ.get('PORT', 9001))
PORT = int(os.environ['PORT']) if 'PORT' in os.environ else 9001

print(PORT)

import os


PORT = int(os.environ.get('PORT')) if 'PORT' in os.environ else 9001

print(PORT)

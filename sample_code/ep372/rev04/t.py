import pkgutil

import pkg

print(pkg.__path__)

for _, name, _ in pkgutil.walk_packages(pkg.__path__, f'{pkg.__name__}.'):
    print(name)

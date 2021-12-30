import pkgutil

import pkg

print(pkg.__path__)

for modinfo in pkgutil.walk_packages(pkg.__path__, f'{pkg.__name__}.'):
    print(modinfo)

import pkgutil

import pkg

print(pkg.__path__)

for modinfo in pkgutil.walk_packages(pkg.__path__):
    print(modinfo)

import unicodedata

for i in range(65535):
    try:
        c = chr(i)
    except Exception:
        pass

    if c.lower() != c.casefold():
        print('===')
        print(f'{i:x}')
        print(f'{c.lower()}: {unicodedata.name(c.lower())}')
        for c2 in c.casefold():
            print(f'* {c2}: {unicodedata.name(c2)}')

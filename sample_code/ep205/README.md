# [python: str.translate (intermediate)](https://youtu.be/0kYctEx_O28)

Тoday I talk about the `str.translate` / `str.maketrans` methods as well as a quick use case on how you might use them!

## Interactive examples

### Python

```python
s = 'hello world <script>alert("hi");</script>'
table = {ord('<'): '&lt;', ord('>'): '&gt;', ord('"'): '&quot;', ord('&'): '&amp;'}
s.translate(table)

table = str.maketrans({'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'})
s.translate(table)
s.translate(table).translate(table)

import string
table_upper = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)
'hello hello wolrd'.translate(table_upper)

table_upper = str.maketrans(string.ascii_lowercase, string.ascii_uppercase, string.punctuation)
'hello!  hello!  world!'.translate(table_upper)

hex(ord('c'))


class HexEncode():
    def __getitem__(self, c: int) -> str:
        return hex(c)


'hello hello world'.translate(HexEncode())


class HexEncode():
    def __getitem__(self, c: int) -> str:
        return hex(c)[2:]


'hello hello world'.translate(HexEncode())
'\u2603'.translate(HexEncode())
```

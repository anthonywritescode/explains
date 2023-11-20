# [what is a BOM (byte-order-marker) (intermediate)](https://youtu.be/OrtNMystCgM)

Today we talk about the UTF family of encodings and the BOM -- and why you probably don't want it and shouldn't need it!

## Interactive examples

### Python

```python
'_'.join(bin(c) for c in '☃'.encode())
'_'.join(bin(c) for c in 'A'.encode())
'_'.join(bin(c) for c in '🙃'.encode())

'_'.join(bin(c) for c in '🙃'.encode('utf-16le'))
'_'.join(bin(c) for c in '🙃'.encode('utf-16be'))

'\u2603'
'\u2603'.encode('utf-16le')
'\u2603'.encode('utf-16be')
'\u2603'.encode('utf-32')

len('\u2603'.encode('utf-32'))
len('\u2603'.encode('utf-32le'))
len('\u2603'.encode('utf-32be'))

'\u2603'.encode('utf-16')
'\u2603'.encode('utf-16be')
'\u2603'.encode('utf-16le')

with open('f', 'w', encoding='utf-16le') as f:
    f.write('\u2603')

with open('f', 'w', encoding='utf-8-sig') as f:
    f.write('\u2603foo')
```

### Bash

```bash
python3

hd -c f
```

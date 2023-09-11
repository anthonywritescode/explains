# [what is `Symbol` in js (intermediate)](https://youtu.be/gZBQ8LIR6D4)

I recently was writing some JS and wondered what `Symbol` was -- and now that I know I'm sharing it with you

## Interactive examples

### JavaScript

```javascript
JSON.stringify({foo: 'hello'})
o = {toJSON: () => {return {hello: 'hello world'}}}
JSON.stringify(o)

Symbol

o = {[Symbol.iterator]: function* () { yield 1; yield 2; yield 3; }}

for (let i of o) {
    console.log(i);
}

o.iterator
o[Symbol.iterator]

let fooSymbol = Symbol('foo')
fooSymbol

Symbol('foo') == fooSymbol
Symbol('foo') === fooSymbol

let globalFoo = Symbol.for('foo')
globalFoo == fooSymbol

globalFoo == Symbol.for('foo')
globalFoo === Symbol.for('foo')

Symbol.keyFor(fooSymbol)
Symbol.keyFor(Symbol.iterator)
Symbol.keyFor(globalFoo)
```

### Bash

```bash
node
```

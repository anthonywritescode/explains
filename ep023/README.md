# [introduction to markdown (beginner)](https://youtu.be/1UodxuXj5Ao)

Today I go over some basics with markdown (as well as some tips and tricks!).  Given how pervasive markdown is in open source, documentation, chat clients, etc. I hope this is useful!

## Interactive Markdown examples

### Lists

```markdown
- lists (unordered and numbered)
- checkboxes
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

```markdown
- lists (unordered and numbered)
  - indented
  - item
- checkboxes
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

```markdown
- lists (unordered and numbered)

test test

  - indented
  - item
- checkboxes
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

```markdown
- lists (unordered and numbered)

  test test

  - indented
  - item
- checkboxes
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

```markdown
- lists (unordered and numbered)

  test test

  * indented
  * item

1. foo
2. bar
3. baz

- checkboxes
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

```markdown
- lists (unordered and numbered)

  test test

  * indented
  * item

0. foo
0. bar
0. baz

- checkboxes
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

```markdown
- lists (unordered and numbered)

  test test

  * indented
  * item

1. foo
1. quax
1. bar
1. baz

- checkboxes
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

### Checkboxes

```markdown
- checkboxes
  - required item 1
  - required item 2
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

```markdown
- checkboxes
  - [x] required item 1
  - [ ] required item 2
- fixed width text
- code blocks
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

### Code blocks

```markdown
- code blocks


      print('hello world')
      print('my name is anthony')


- fixed width text
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
```

~~~markdown
- code blocks

   ```python
   print('hello world')
   print('my name is anthony')
   ```

   ```pycon
   >>> print('hello world')
   hello world
   ```

   ```console
   $ echo hi
   hi
   ```

- fixed width text
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
~~~

### Fixed width text

~~~markdown
- fixed width text: `pip install pre-commit`
`
foo
bar
baz
`
- headers
- links (inline and reference)
- images
- bold / italic
- quotes
~~~

### Headers

```markdown
- headers
# this is a h1
# this is a h2
# this is a h3
# this is even deeper

this is a header
================

this is a header
----------------


- links (inline and reference)
- images
- bold / italic
- quotes
```

### Links

```markdown
- links (inline and reference)


[go visit pre-commit.com!](https://pre-commit.com)


go visit [@asottile]'s [github] profile


[@asottile]: https://github.com/asottile
[github]: https://github.com

- images
- bold / italic
- quotes
```

### Images

```markdown
- images


![cat saying shipit high five](https://i.fluffy.cc/MKjDMmwXxZlqRTwnn070gVqZ8Rwh6d3p.gif)


- bold / italic
- quotes
```

### Bold / Italic

```markdown
- **bold** / _italic_
- quotes
```

### Quotes

```markdown
- quotes


> > you should fix this !
>
> it would be better if you used a semicolon


ok I have fixed it
```

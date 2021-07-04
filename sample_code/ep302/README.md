# [bash: strings with `!` / !... event not found (beginner - intermediate) anthony explains](https://youtu.be/VkRjT3UBiLk)

Today I talk about how to use strings with `!` in them as well as the differences between hard quotes and soft quotes!

## Interactive examples

### Bash

```bash
git init x
cd !$
git commit --allow-empty -m "Implement the !donate command"

# watch <some command>
echo "!wat"

git commit --allow-empty -m 'Implement the !donate command'
git show

git commit --allow-empty -m 'Implement the !donate command $USER'
echo "$USER"

git commit --allow-empty -m 'Implement the !donate command'" $USER"
```

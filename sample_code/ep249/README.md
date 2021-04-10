# [PS1, coloring, and fixing weird wrapping (beginner - intermediate)](https://youtu.be/ngLwml9XI-I)

Today I talk a little bit about bash prompts and PS1 as well as how to color it (and properly!)

## Interactive examples

### Bash

```bash
PS1='hello hello$ '
echo hi

echo -e '\033[43mhellohello\033[m'
PS1='\033[43mhello hello\033[m$ '

PS1='\[\033[43m\]hello hello\[\033[m\]$ '

nano ~/.bashrc
PS1='\[\033[43m\]hello hello\[\033[m\]:\w$ '
PS1='\u:\[\033[43m\]hello hello\[\033[m\]:\w$ '
PS1='\u@\h:\[\033[43m\]hello hello\[\033[m\]:\w$ '
```

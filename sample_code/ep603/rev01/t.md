```c
int fac(int n) {
    if (n == 1) return 1;
    return n * fac(n - 1);
}
```

```
fac(3) =>
3 * fac(2) =>
3 * 2 * fac(1) =>
3 * 2 * 1 => 6
```

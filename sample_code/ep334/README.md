# [what is "idempotent" in programming (beginner)](https://youtu.be/o9THkT5ZPi4)

Today I go over what "idempotent" means in programming as well as a few common examples!

## Interactive examples

### Bash

```bash
mkdir a
ls

mkdir a
echo $?

mkdir -p a
mkdir --parents a
mkdir --parents a/b/c/d
tree .

mkdir --parents a/b/c/d
echo $?

rmdir -p a/b/c/d
ls

rm -rf a/b/c/d
echo $?

touch a
rm -f a
rm -f a

sqlite3
```

### Sqlite3

```sql
CREATE TABLE USERS (username, age);

INSERT INTO USERS VALUES ('john', 24);

-- /update_age?user=...&age=...^

UPDATE USERS SET age = 25 WHERE username = 'john';
SELECT * FROM USERS;

UPDATE USERS SET age = 25 WHERE username = 'john';
SELECT * FROM USERS;
```

# [sqlite is my favorite database (beginner - intermediate)](https://youtu.be/jH39c5-y6kg)

Today I talk about sqlite -- how to get started with it, where you should use it, and why I like it so much!

## Interactive examples

### Bash

```bash
sqlite3 :memory:
sqlite3 db.db

ls
file db.db

sqlite3 db.db 'select * from wat;'
seq 1 10 | xargs -P 5 --replace sqlite3 db.db 'insert into wat values ({});'
sqlite3 db.db 'select * from wat;'

git clone git@github.com:asottile/astpretty
cd astpretty/
tox -e py38
sqlite3 .coverage
```

### SQLite

```sql
create table wat (a);
insert into wat values (1);
select * from wat;

.schema

.headers on
select * from wat;
.help
.quit
.exit
```

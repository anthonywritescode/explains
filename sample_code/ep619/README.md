# [sqlite: STRING is actually an integer type???](https://youtu.be/VSiPVZcTQTo)

today I show a quirk with sqlite's type compatibility and a useful fix!

## Interactive examples

### Bash

```bash
sqlite3
```

### SQLite

```sql
CREATE TABLE t (s STRING);
INSERT INTO t VALUES ('  123  ');

select * FROM t;
select typeof(s) FROM t;

CREATE TABLE t2 (s asdfasdf);
CREATE TABLE t3 (s);
CREATE TABLE t4 (s) STRICT;
CREATE TABLE t4 (s STRING) STRICT;
CREATE TABLE t4 (s TEXT) STRICT;
CREATE TABLE t5 (s VARCHAR) STRICT;
```

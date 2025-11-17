# SQL: DDL & DML

## DDL (for Data Definition)

- Main concerns for DDL are
  - Create Database, Table, Columns
  - Rename Database, Rename Table
  - Alter Table, Alter Columns
  - Drop Database, Drop Table, Drop Columns
  - Truncate Table

### Create Database

```postgresql
CREATE DATABASE database_name;
```

**Notes**

- rules for **database, table, and column name**
  - must not contains `spaces` or any other symbols, except `_` (underscore).
  - the **first** character must be **alphabet**, the other characters can be **alphanumeric** or `_`.
  - all names are **lowercase** by default.
- to **override** the naming rules, you can use `"` (double quotes), for example `"1Database Name"`.
- **Every SQL statement** must ends with `;` (semicolon)

### Create Table

```postgresql
CREATE TABLE [IF NOT EXISTS] tbl_name (
    column_name1 data_type [constraint],
    column_name2 data_type [constraint],
    ...
    column_nameN data_type [constraint]
);
```

**Notes**

- contraints:
  - `PRIMARY KEY`
  - `UNIQUE`
  - `NOT NULL`
- for more contraints reference [click here](https://www.postgresql.org/docs/current/ddl-constraints.html)

### Alter

#### Alter Database / Rename Database

```postgresql
ALTER DATABASE old_name RENAME TO new_name;
```

> for more alter database reference [click here](https://www.postgresql.org/docs/current/sql-alterdatabase.html)

#### Alter Table

##### Rename Table

```postgresql
ALTER TABLE old_name
RENAME TO new_name;
```

##### Rename Column

```postgresql
ALTER TABLE tbl_name
RENAME COLUMN old_name TO new_name;
```

##### Change Column's data type

```postgresql
ALTER TABLE tbl_name
ALTER COLUMN col_name TYPE data_type;
```

##### Add new Column

```postgresql
ALTER TABLE tbl_name
ADD COLUMN col_name data_type [constraint];
```

##### Drop Column

```postgresql
ALTER TABLE tbl_name
DROP COLUMN col_name;
```

> for more alter table reference [click here](https://www.postgresql.org/docs/current/sql-altertable.html)

### Drop

#### Drop Database

```postgresql
DROP DATABASE database_name;
```

#### Drop Table

```postgresql
DROP TABLE [IF EXISTS] tbl_name;
```

### Truncate

```postgresql
TRUNCATE TABLE tbl_name;
```

## DML (for Data Manipulation)

- Main concerns for DML are
  - Insert data
  - Update data
  - Delete data

### Insert

```postgresql
INSERT INTO tbl_name [ (column1, column2, ..., columnN) ]
VALUES (value1, value2, ..., valueN);
```

#### Bulk/Multiple Insert

```postgresql
INSERT INTO tbl_name [ (column1, column2, ..., columnN) ]
VALUES (value1, value2, ..., valueN), 
(value1, value2, ..., valueN), 
(value1, value2, ..., valueN);
```

### Update

```postgresql
UPDATE tbl_name
SET col_name = new_value
WHERE condition;
```

### Delete

```postgresql
DELETE FROM tbl_name
WHERE condition;
```

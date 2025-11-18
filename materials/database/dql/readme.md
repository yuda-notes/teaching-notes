# SQL: DQL

## DQL (for Data Query)

- is used for retreiving data from table

<img src="https://assets.bytebytego.com/diagrams/0114-sql-query-logical-order.png" width="500">

### Basic form

```postgresql
SELECT * FROM tbl_name;

SELECT column1 FROM tbl_name;

SELECT column1, column2, ..., columnN FROM tbl_name;
```

### With column alias

```postgresql
SELECT column1 AS column_one FROM tbl_name;

SELECT column1 AS "Column 1" FROM tbl_name;
```

### Distinct

- to get unique values from specific columns

```postgresql
SELECT DISTINCT column1 FROM tbl_name;

-- this will return unique pair of values between column1 and column2
SELECT DISTINCT column1, column2 FROM tbl_name;
```

### `WHERE` clause / Filter data

- comparison operators `= != <> > >= < <= BETWEEN...AND... IN LIKE ILIKE NOT`

```postgresql
SELECT * FROM tbl_name WHERE condition;
```

### `GROUP BY` clause / Aggregate data

- Aggregate functions:
  - `COUNT()`
  - `SUM()`
  - `AVG()`
  - `MIN()`
  - `MAX()`

```postgresql
SELECT SUM(column1)
FROM tbl_name
GROUP BY column2;
```

#### `HAVING` clause

- same like `WHERE` but **only** works for aggregate functions

    ```postgresql
    SELECT column1
    FROM tbl_name
    GROUP BY column1
    HAVING condition;
    ```

### `ORDER BY` / Sort data

```postgresql
SELECT * FROM tbl_name
ORDER BY column1;
```

### Join tables

```postgresql
SELECT * 
FROM tbl_name1
JOIN tbl_name2 
ON tbl_name1.col_name = tbl_name2.col_name;
```

<img src="https://www.codeproject.com/_next/image?url=https%3A%2F%2Fcloudfront.codeproject.com%2Fdatabase%2Fvisual_sql_joins%2Fvisual_sql_joins_v2.png&w=1200&q=75" width="500">

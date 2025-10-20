# Database

## Definition

- Database is a place to permanently store data
- There are 3 types of data
  - Unstructured Data -> `text`, `article`, `news`, etc.
  - Semi-structured Data -> `profile`, `social media post`, etc.
  - Structured Data -> `financial report`, `marketplace transaction`, etc.

## Database Types

- Based on processing
  - OLTP -> can **read** and **write** (transactional)
  - OLAP -> **read-only** (Data Warehouse)
    <img src="https://www.boardinfinity.com/blog/content/images/2023/05/OLAP-VS-OLTP.png" width=100%>
- Based on data relationship
  - Relational Database (SQL) -> `PostgreSQL`, `MySQL`, etc.
  - Non-relational Database (NoSQL) -> `MongoDB`, `ElasticSearch`, etc.
    <img src="https://existek3-838c.kxcdn.com/wp-content/uploads/2022/09/3-8.webp" width=100%>

## Relational Database

- Database that consist of **structured** data in the form of **Table**.
- Each table have **Rows** and **Columns**.
- Uses **SQL** as programming language
- Table constraints ([reference](https://www.geeksforgeeks.org/sql/sql-constraints/)):
  - **Primary Key** -> one or more columns that uniquely identifies each row.
  - **Foreign Key** -> a column that create a relationship between two tables.
  - etc.

## ERD

- **ERD** or Entity Relationship Diagram, is a visualization of table relationships inside database.
- There are 3 types of relationship

  - **one-to-one** (1:1)
  - **one-to-many** (1:n)
  - **many-to-many** (m:n)
    <img src="https://cdn-images.visual-paradigm.com/guide/data-modeling/what-is-erd/14-erd-example-loan-system.png" width=100%>
    <img src="https://runestone.academy/ns/books/published/practical_db/_images/subset_of_ERD.svg" width=100%>

## Normalization

- Normalization is a process of organizing table to reduce redundancy and improve data integrity
- There are 3 levels normalization, from **1NF** to **3NF**. Each levels have specific criteria that needs to be required before proceed to next step.
  1. 1NF
     - Each row must be unique (have Primary Key)
     - Each column must contain atomic values
  2. 2NF
     - Passed 1NF
     - All **non-key** columns must be **fully functionally dependent** on the **Primary Key**
  3. 3NF
     - Passed 3NF
     - **No transitive dependency**

### Dependency

- **Dependency** is a logical relationship between **columns** in each table.

  | ProductID | ProductName |
  | --------- | ----------- |
  | X123      | ProductXYZ  |
  | ABC99     | ProductABC  |
  | ...       | ...         |

  > From the example above, we can see that **ProductName** is dependent on **ProductId** (Primary Key). So every time we see id `X123` again, we know that the product name will be `ProductXYZ`. This is **DEPENDENCY** `(Column1 -> Column2)`.

- Types of Dependency
  - Full Dependency
  - Partial Dependency
  - Transitive Dependency
    <img src="https://media.cheggcdn.com/media/2ca/2ca85cfc-e2ee-4fd6-8637-6e5ef12c4c95/php59ZDG0" width=100%>

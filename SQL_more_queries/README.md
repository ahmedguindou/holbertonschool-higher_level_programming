# MySQL Basics

## 📌 Table of Contents
- [How to Create a New MySQL User](#how-to-create-a-new-mysql-user)
- [How to Manage Privileges](#how-to-manage-privileges)
- [Primary Key](#primary-key)
- [Foreign Key](#foreign-key)
- [NOT NULL & UNIQUE Constraints](#not-null--unique-constraints)
- [Retrieving Data from Multiple Tables](#retrieving-data-from-multiple-tables)
- [Subqueries](#subqueries)
- [JOIN vs UNION](#join-vs-union)

---

## 🔹 How to Create a New MySQL User
```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```
**Example:**
```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'securePass123';
```

---

## 🔹 How to Manage Privileges
Grant full access:
```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';
FLUSH PRIVILEGES;
```
Revoke privileges:
```sql
REVOKE SELECT, INSERT ON database_name.* FROM 'username'@'host';
FLUSH PRIVILEGES;
```

---

## 🔹 Primary Key
A **PRIMARY KEY** uniquely identifies each row.
```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
```
With auto-increment:
```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
```

---

## 🔹 Foreign Key
A **FOREIGN KEY** links two tables.
```sql
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```
To delete associated records:
```sql
FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE;
```

---

## 🔹 NOT NULL & UNIQUE Constraints
Prevent NULL values:
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```
Ensure uniqueness:
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE
);
```

---

## 🔹 Retrieving Data from Multiple Tables
```sql
SELECT users.name, orders.order_id
FROM users
JOIN orders ON users.id = orders.user_id;
```

### **Types of JOINs**
| JOIN Type | Description |
|-----------|-------------|
| `INNER JOIN` | Returns **only matching** rows. |
| `LEFT JOIN` | Returns **all rows from the left table**, even if there's **no match** in the right table. |
| `RIGHT JOIN` | Returns **all rows from the right table**, even if there's **no match** in the left table. |
| `FULL JOIN` | Returns **all rows** when there's a match in either table. |

**Example:**
```sql
SELECT users.name, orders.order_id
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

---

## 🔹 Subqueries
A query inside another query.
```sql
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE amount > 100);
```

---

## 🔹 JOIN vs UNION
**JOIN:** Combines columns from multiple tables.
```sql
SELECT users.name, orders.order_id
FROM users
JOIN orders ON users.id = orders.user_id;
```

**UNION:** Combines rows from multiple queries.
```sql
SELECT name FROM old_customers
UNION
SELECT name FROM new_customers;
```
*Note: `UNION` removes duplicates by default; use `UNION ALL` to keep them.*

---

## 🚀 Quick Recap
| Concept | Meaning |
|---------|---------|
| `CREATE USER` | Creates a new MySQL user. |
| `GRANT PRIVILEGES` | Gives permissions to a user. |
| `PRIMARY KEY` | Ensures each row has a unique identifier. |
| `FOREIGN KEY` | Links two tables together. |
| `NOT NULL & UNIQUE` | Prevents empty or duplicate values. |
| `JOIN` | Combines data from multiple tables. |
| `UNION` | Combines results from multiple queries. |
| `Subqueries` | A query inside another query. |


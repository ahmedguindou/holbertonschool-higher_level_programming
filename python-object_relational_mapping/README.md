# MySQL with Python

## Description
This project focuses on connecting a Python script to a MySQL database, performing CRUD operations, and understanding Object-Relational Mapping (ORM) using SQLAlchemy.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without external references:
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python class to a MySQL table

## Requirements
- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQL server (version 5.7 or higher recommended)
- MySQLdb (version 2.0.x)
- SQLAlchemy (version 1.4.x)
- Code should follow `pycodestyle` (version 2.7.*)
- All files must be executable (`chmod +x filename.py`)
- Use `vi`, `vim`, or `emacs` for editing

## Installation
### Install MySQL Server (if not installed)
```bash
sudo apt update
sudo apt install mysql-server
```

### Install Required Python Packages
```bash
pip install MySQL-python  # For MySQLdb
pip install SQLAlchemy==1.4.*
```

## Usage

### 1. Connecting to MySQL using MySQLdb
```python
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="your_username",
    passwd="your_password",
    db="your_database"
)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
print(cursor.fetchone())

db.close()
```

### 2. Selecting Data with MySQLdb
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

### 3. Inserting Data with MySQLdb
```python
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John Doe", 30))
db.commit()
```

### 4. Using SQLAlchemy ORM
#### Define a Model
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

engine = create_engine('mysql+mysqldb://username:password@localhost/database')
Base.metadata.create_all(engine)
```

#### Querying with SQLAlchemy
```python
Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()
for user in users:
    print(user.name, user.age)
```

## Author
- Vision

## License
This project is licensed under the MIT License.

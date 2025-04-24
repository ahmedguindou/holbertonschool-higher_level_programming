# Python Object Basics
---

## 🧱 What is an Object?
In Python, **everything is an object**. An object has:
- A **type** (e.g., int, str)
- A **value**
- An **identifier** (its memory address)

```python
x = 7  # 'x' refers to an object of type int with value 7
```

---

## 🧹 Class vs Object (Instance)
- **Class**: A blueprint or template.
- **Object**: An instance created from a class.

```python
class Car:
    pass

my_car = Car()  # Object (instance of Car)
```

---

## 🔒🔓 Immutable vs Mutable Objects
- **Immutable**: Cannot be changed after creation.
- **Mutable**: Can be changed.

### Immutable Example:
```python
x = "hello"
x[0] = "H"  # Error – strings are immutable
```

### Mutable Example:
```python
my_list = [1, 2, 3]
my_list[0] = 10  # Works – lists are mutable
```

---

## 🪯 What is a Reference?
A reference is a label that points to an object in memory.
```python
a = [1, 2, 3]  # 'a' refers to the list object
```

---

## ➡️ What is an Assignment?
Assignment is using `=` to bind a variable to an object.
```python
x = 10
```

---

## 🪞 What is an Alias?
An alias is another name pointing to the same object.
```python
a = [1, 2]
b = a  # b is an alias for a
b.append(3)
print(a)  # [1, 2, 3]
```

---

## 🆔 How to Know if Two Variables Are Identical?
Use the `is` keyword:
```python
a = [1, 2]
b = a
print(a is b)  # True
```

---

## 🔗 How to Know if Two Variables Reference the Same Object?
Again, use `is`:
```python
x = 5
y = 5
print(x is y)  # True (for small integers)
```

---

## 📍 How to Display the Variable Identifier?
Use `id()`:
```python
a = 42
print(id(a))
```

---

## 🔄 Mutable vs Immutable Recap

| Type       | Can be changed? | Examples                |
|------------|------------------|-------------------------|
| Mutable    | ✅ Yes           | `list`, `dict`, `set`     |
| Immutable  | ❌ No            | `int`, `str`, `tuple`     |

---

## 🛠️ Built-in Mutable Types
- `list`
- `dict`
- `set`
- `bytearray`

---

## 🔐 Built-in Immutable Types
- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `frozenset`
- `bytes`

---

## 🚚 How Does Python Pass Variables to Functions?
Python uses **pass-by-object-reference** (a.k.a. pass-by-sharing).

### Immutable Example:
```python
def change(x):
    x = 10

a = 5
change(a)
print(a)  # 5 – unchanged
```

### Mutable Example:
```python
def modify(lst):
    lst.append(4)

nums = [1, 2, 3]
modify(nums)
print(nums)  # [1, 2, 3, 4]
```

# Python List Methods Cheat Sheet

### .append()
- **Purpose:** Add an element to the end of a list.
- **Syntax:** `list.append(item)`
- **Example:**
  ```python
  fruits = ['apple', 'banana']
  fruits.append('cherry')  # Result: ['apple', 'banana', 'cherry']


### .pop()
- **Purpose:** Remove and return an element from a list.
- **Syntax:** 
   - Default (last element): list.pop()
   - Specific index: list.pop(index)
```python
fruits = ['apple', 'banana', 'cherry']
last = fruits.pop()      # last = 'cherry', fruits = ['apple', 'banana']
first = fruits.pop(0)    # first = 'apple', fruits = ['banana']


### .split()
- **Purpose:** Divides a string into a list of substrings based on a separator.
- **Syntax:** `string.split(separator, maxsplit)`
- **Example:**
  ```python
  text = "apple,banana,cherry"
  fruits = text.split(',')  # Result: ['apple', 'banana', 'cherry']
  
  sentence = "Python is awesome"
  words = sentence.split()  # Result: ['Python', 'is', 'awesome']
  
  numbers = "1-2-3-4-5"
  first_two = numbers.split('-', 2)  # Result: ['1', '2', '3-4-5']
  ```

### .join()
- **Purpose:** Combines a list of strings into a single string using a specified delimiter.
- **Syntax:** `delimiter.join(iterable)`
- **Example:**
  ```python
  fruits = ['apple', 'banana', 'cherry']
  text = ','.join(fruits)  # Result: 'apple,banana,cherry'
  
  words = ['Python', 'is', 'awesome']
  sentence = ' '.join(words)  # Result: 'Python is awesome'
  
  path_parts = ['usr', 'local', 'bin']
  path = '/'.join(path_parts)  # Result: 'usr/local/bin'
  ```

### .strip()
- **Purpose:** Removes leading and trailing characters (spaces by default).
- **Syntax:** `string.strip(chars)`
- **Example:**
  ```python
  text = "  Hello, World!  "
  cleaned = text.strip()  # Result: 'Hello, World!'
  
  price = "$100.00$"
  number = price.strip('$')  # Result: '100.00'
  
  filename = "###report.txt###"
  clean_name = filename.strip('#')  # Result: 'report.txt'
  ```

### .replace()
- **Purpose:** Replaces occurrences of a substring with another substring.
- **Syntax:** `string.replace(old, new, count)`
- **Example:**
  ```python
  text = "Hello, World!"
  new_text = text.replace("Hello", "Hi")  # Result: 'Hi, World!'
  
  sentence = "I like apples, apples are tasty"
  new_sentence = sentence.replace("apples", "oranges", 1)  # Result: 'I like oranges, apples are tasty'
  
  code = "x = 10; y = 20; z = 30;"
  python_code = code.replace(";", "")  # Result: 'x = 10 y = 20 z = 30'
  ```

# Additional Python Functions Cheatsheet

## String Methods

### .startswith()
- **Purpose:** Check if a string starts with specified prefix.
- **Syntax:** `string.startswith(prefix, start, end)`
- **Example:**
  ```python
  filename = "document.pdf"
  is_doc = filename.startswith("doc")  # Result: True
  is_txt = filename.startswith("txt")  # Result: False
  ```

### .endswith()
- **Purpose:** Check if a string ends with specified suffix.
- **Syntax:** `string.endswith(suffix, start, end)`
- **Example:**
  ```python
  filename = "report.pdf"
  is_pdf = filename.endswith(".pdf")  # Result: True
  is_doc = filename.endswith(".doc")  # Result: False
  ```

### .upper()
- **Purpose:** Convert string to uppercase.
- **Syntax:** `string.upper()`
- **Example:**
  ```python
  text = "Hello"
  upper_text = text.upper()  # Result: 'HELLO'
  ```

### .lower()
- **Purpose:** Convert string to lowercase.
- **Syntax:** `string.lower()`
- **Example:**
  ```python
  text = "Hello"
  lower_text = text.lower()  # Result: 'hello'
  ```

### .title()
- **Purpose:** Convert first character of each word to uppercase.
- **Syntax:** `string.title()`
- **Example:**
  ```python
  text = "hello world"
  title_text = text.title()  # Result: 'Hello World'
  ```

### .capitalize()
- **Purpose:** Convert first character to uppercase, rest to lowercase.
- **Syntax:** `string.capitalize()`
- **Example:**
  ```python
  text = "hello WORLD"
  cap_text = text.capitalize()  # Result: 'Hello world'
  ```

### .count()
- **Purpose:** Count occurrences of a substring.
- **Syntax:** `string.count(substring, start, end)`
- **Example:**
  ```python
  text = "apple apple orange"
  count = text.count("apple")  # Result: 2
  ```

### .find()
- **Purpose:** Find first occurrence of substring (returns -1 if not found).
- **Syntax:** `string.find(substring, start, end)`
- **Example:**
  ```python
  text = "Hello World"
  position = text.find("World")  # Result: 6
  not_found = text.find("Python")  # Result: -1
  ```

### .index()
- **Purpose:** Find first occurrence of substring (raises ValueError if not found).
- **Syntax:** `string.index(substring, start, end)`
- **Example:**
  ```python
  text = "Hello World"
  position = text.index("World")  # Result: 6
  # text.index("Python")  # Raises ValueError
  ```

### .isdigit()
- **Purpose:** Check if all characters are digits.
- **Syntax:** `string.isdigit()`
- **Example:**
  ```python
  num = "12345"
  text = "abc123"
  num_check = num.isdigit()  # Result: True
  text_check = text.isdigit()  # Result: False
  ```

### .isalpha()
- **Purpose:** Check if all characters are alphabetic.
- **Syntax:** `string.isalpha()`
- **Example:**
  ```python
  text = "Python"
  mixed = "Python3"
  alpha_check = text.isalpha()  # Result: True
  mixed_check = mixed.isalpha()  # Result: False
  ```

### .isalnum()
- **Purpose:** Check if all characters are alphanumeric.
- **Syntax:** `string.isalnum()`
- **Example:**
  ```python
  text = "Python3"
  with_space = "Python 3"
  alnum_check = text.isalnum()  # Result: True
  space_check = with_space.isalnum()  # Result: False
  ```

## List Methods

### .insert()
- **Purpose:** Insert an item at a specified position.
- **Syntax:** `list.insert(index, item)`
- **Example:**
  ```python
  fruits = ['apple', 'cherry']
  fruits.insert(1, 'banana')  # Result: ['apple', 'banana', 'cherry']
  ```

### .pop()
- **Purpose:** Remove and return an item at specified position (last by default).
- **Syntax:** `list.pop(index)`
- **Example:**
  ```python
  fruits = ['apple', 'banana', 'cherry']
  last = fruits.pop()  # Result: 'cherry', fruits becomes ['apple', 'banana']
  first = fruits.pop(0)  # Result: 'apple', fruits becomes ['banana']
  ```

### .remove()
- **Purpose:** Remove first occurrence of a value.
- **Syntax:** `list.remove(value)`
- **Example:**
  ```python
  fruits = ['apple', 'banana', 'apple', 'cherry']
  fruits.remove('apple')  # Result: ['banana', 'apple', 'cherry']
  ```

### .sort()
- **Purpose:** Sort list in-place.
- **Syntax:** `list.sort(key=None, reverse=False)`
- **Example:**
  ```python
  numbers = [3, 1, 4, 2]
  numbers.sort()  # Result: [1, 2, 3, 4]
  
  # Sort by length
  words = ['apple', 'banana', 'fig']
  words.sort(key=len)  # Result: ['fig', 'apple', 'banana']
  ```

### sorted()
- **Purpose:** Return a new sorted list.
- **Syntax:** `sorted(iterable, key=None, reverse=False)`
- **Example:**
  ```python
  numbers = [3, 1, 4, 2]
  sorted_nums = sorted(numbers)  # Result: [1, 2, 3, 4], numbers still [3, 1, 4, 2]
  
  # Sort descending
  desc_nums = sorted(numbers, reverse=True)  # Result: [4, 3, 2, 1]
  ```

### .extend()
- **Purpose:** Add all items from another iterable to the list.
- **Syntax:** `list.extend(iterable)`
- **Example:**
  ```python
  fruits = ['apple', 'banana']
  more_fruits = ['cherry', 'date']
  fruits.extend(more_fruits)  # Result: ['apple', 'banana', 'cherry', 'date']
  ```

## Dictionary Methods

### .get()
- **Purpose:** Return value for key, or default if key doesn't exist.
- **Syntax:** `dict.get(key, default=None)`
- **Example:**
  ```python
  user = {'name': 'John', 'age': 30}
  name = user.get('name')  # Result: 'John'
  email = user.get('email', 'Not set')  # Result: 'Not set'
  ```

### .update()
- **Purpose:** Update dictionary with key/value pairs from another.
- **Syntax:** `dict.update(other_dict)`
- **Example:**
  ```python
  user = {'name': 'John', 'age': 30}
  more_info = {'email': 'john@example.com', 'age': 31}
  user.update(more_info)  # Result: {'name': 'John', 'age': 31, 'email': 'john@example.com'}
  ```

### .items()
- **Purpose:** Return view object of dictionary's (key, value) pairs.
- **Syntax:** `dict.items()`
- **Example:**
  ```python
  user = {'name': 'John', 'age': 30}
  for key, value in user.items():
      print(f"{key}: {value}")  # Prints "name: John" and "age: 30"
  ```

### .keys()
- **Purpose:** Return view object of dictionary's keys.
- **Syntax:** `dict.keys()`
- **Example:**
  ```python
  user = {'name': 'John', 'age': 30}
  keys = list(user.keys())  # Result: ['name', 'age']
  ```

### .values()
- **Purpose:** Return view object of dictionary's values.
- **Syntax:** `dict.values()`
- **Example:**
  ```python
  user = {'name': 'John', 'age': 30}
  values = list(user.values())  # Result: ['John', 30]
  ```

## File Operations

### open()
- **Purpose:** Open a file and return a file object.
- **Syntax:** `open(file, mode='r', encoding=None)`
- **Example:**
  ```python
  # Read file content
  with open('example.txt', 'r') as file:
      content = file.read()
  
  # Write to file
  with open('example.txt', 'w') as file:
      file.write('Hello, World!')
  ```

### .read()
- **Purpose:** Read entire file content.
- **Syntax:** `file.read(size=-1)`
- **Example:**
  ```python
  with open('example.txt', 'r') as file:
      content = file.read()  # Read entire file
      partial = file.read(10)  # Read next 10 characters
  ```

### .readline()
- **Purpose:** Read one line from file.
- **Syntax:** `file.readline()`
- **Example:**
  ```python
  with open('example.txt', 'r') as file:
      first_line = file.readline()
      second_line = file.readline()
  ```

### .readlines()
- **Purpose:** Read all lines into a list.
- **Syntax:** `file.readlines()`
- **Example:**
  ```python
  with open('example.txt', 'r') as file:
      lines = file.readlines()  # Result: ['Line 1\n', 'Line 2\n', ...]
  ```

### .write()
- **Purpose:** Write string to file.
- **Syntax:** `file.write(string)`
- **Example:**
  ```python
  with open('example.txt', 'w') as file:
      chars_written = file.write('Hello, World!')  # Result: 13
  ```

### .writelines()
- **Purpose:** Write list of strings to file.
- **Syntax:** `file.writelines(list_of_strings)`
- **Example:**
  ```python
  with open('example.txt', 'w') as file:
      file.writelines(['Line 1\n', 'Line 2\n', 'Line 3\n'])
  ```

## Utility Functions

### enumerate()
- **Purpose:** Return an enumerated object (index, value pairs).
- **Syntax:** `enumerate(iterable, start=0)`
- **Example:**
  ```python
  fruits = ['apple', 'banana', 'cherry']
  for index, fruit in enumerate(fruits):
      print(f"{index}: {fruit}")  # Prints "0: apple", "1: banana", "2: cherry"
  
  # Start from 1
  for index, fruit in enumerate(fruits, start=1):
      print(f"{index}: {fruit}")  # Prints "1: apple", "2: banana", "3: cherry"
  ```

### zip()
- **Purpose:** Combine elements from multiple iterables.
- **Syntax:** `zip(*iterables)`
- **Example:**
  ```python
  names = ['Alice', 'Bob', 'Charlie']
  ages = [25, 30, 35]
  for name, age in zip(names, ages):
      print(f"{name} is {age} years old")
  ```

### any()
- **Purpose:** Return True if any element in iterable is truthy.
- **Syntax:** `any(iterable)`
- **Example:**
  ```python
  values = [False, False, True, False]
  result = any(values)  # Result: True
  
  # Check if any number is even
  numbers = [1, 3, 5, 7, 8]
  has_even = any(num % 2 == 0 for num in numbers)  # Result: True
  ```

### all()
- **Purpose:** Return True if all elements in iterable are truthy.
- **Syntax:** `all(iterable)`
- **Example:**
  ```python
  values = [True, True, True]
  result = all(values)  # Result: True
  
  # Check if all numbers are positive
  numbers = [1, 2, 3, 4, 5]
  all_positive = all(num > 0 for num in numbers)  # Result: True
  ```

### map()
- **Purpose:** Apply function to each item in iterable.
- **Syntax:** `map(function, iterable, ...)`
- **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  squared = list(map(lambda x: x**2, numbers))  # Result: [1, 4, 9, 16]
  
  # Convert strings to integers
  str_nums = ['1', '2', '3']
  nums = list(map(int, str_nums))  # Result: [1, 2, 3]
  ```

### filter()
- **Purpose:** Construct iterator from elements that function returns True.
- **Syntax:** `filter(function, iterable)`
- **Example:**
  ```python
  numbers = [1, 2, 3, 4, 5, 6]
  evens = list(filter(lambda x: x % 2 == 0, numbers))  # Result: [2, 4, 6]
  
  # Filter out empty strings
  words = ['', 'hello', '', 'world']
  non_empty = list(filter(None, words))  # Result: ['hello', 'world']
  ```

### len()
- **Purpose:** Return the length (number of items) of an object.
- **Syntax:** `len(object)`
- **Example:**
  ```python
  text = "Hello"
  length = len(text)  # Result: 5
  
  numbers = [1, 2, 3, 4]
  count = len(numbers)  # Result: 4
  ```

### min()
- **Purpose:** Return smallest item in iterable or smallest of multiple arguments.
- **Syntax:** `min(iterable)` or `min(arg1, arg2, ...)`
- **Example:**
  ```python
  numbers = [5, 3, 8, 2]
  smallest = min(numbers)  # Result: 2
  
  # With key function
  words = ['apple', 'banana', 'fig']
  shortest = min(words, key=len)  # Result: 'fig'
  ```

### max()
- **Purpose:** Return largest item in iterable or largest of multiple arguments.
- **Syntax:** `max(iterable)` or `max(arg1, arg2, ...)`
- **Example:**
  ```python
  numbers = [5, 3, 8, 2]
  largest = max(numbers)  # Result: 8
  
  # With key function
  words = ['apple', 'banana', 'fig']
  longest = max(words, key=len)  # Result: 'banana'
  ```

### sum()
- **Purpose:** Return sum of items in iterable.
- **Syntax:** `sum(iterable, start=0)`
- **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  total = sum(numbers)  # Result: 10
  
  # With start value
  total_plus_10 = sum(numbers, 10)  # Result: 20
  ```
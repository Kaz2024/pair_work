# Pairing challenge Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.

## 2. Design the Function Signature


_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def todo_list(task):
    """
    Parameters: put in the task in a list 

    Returns: the task 

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    return task  # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Create new empty list 
return the empty list 

"""
todo_list([""]) => [""]

"""
Given a task 
It returns the task 
"""
todo_list("walk the dog") => ("walk the dog")

"""
create a list with words
return the words 

"""
todo_list([""walk the dog""]) => ["walk the dog"]

"""
add new task to the list 
return the full list 
"""
todo_list.append("drink water") => ["walk the dog", "drink water"]


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!

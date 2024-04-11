# Complex Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature



```python
def age_check_over_18(age):
return true if user >= 18:

def age_check_under_16(age):
    return false if < 18:

def age_check_over_16_message(age):
    if True:
    return "Access granted"
    else False:
    return "Access denied"

def check_format_entered_incorrectly(age):
    return  with pytest.raises(Exception) as e: "The date of birth isn't the right type or format."
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a birthday 10/4/2005
It returns true 
"""
age_checker("2005-03-26") => True

2024-04-10
#Year #Month #Day

""" 
Given a birthday 11/04/2005
It returns false 
"""
age_checker("2005-04-11") => False

"""
Given date 
It returns message whether if user is old enough
"""

age_output("2005-03-26") => "Access granted!" 
age_output("2005-07-26") => "Access denied!" 

"""
Given invalid format 
return error message 
"""
age_output("26-03-2005") => "The date of birth isn't the right type or format."


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

from lib.age import *
def test_age_over_requirement():


```

Ensure all test function names are unique, otherwise pytest will ignore them!
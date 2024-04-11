from lib.pairing_function import *

# given an empty list 
# return an empty list 

# def test_list_return_empty_list():
#     result = todo_list("")
#     assert result == ("")

# def test_create_an_empty_list():
#     result = todo_list([""])
#     assert result == [""]


# def test_check_if_string_in_list():
#     assert todo_list(["#TODO"]) == ["#TODO"]

# def test_task_in_list():
#     result = todo_list("#TODO walk the dog")
#     assert result == ["#TODO"]

def test_todo_list():
    assert todo_list(["#TODO - Drink water", "Phone"]) == ["#TODO - Drink water"]
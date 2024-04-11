def todo_list(tasks):
    newlist = []
    for task in tasks:
        if "#TODO" in task:
            newlist.append(task)
    return newlist

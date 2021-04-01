def print_task_descriptions(list):
    for task in list:
        print(task["description"])

def print_list(list):
    for task in list:
        print_task(task)

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)
#!/usr/bin/python3
"""Returns info about an employee's TODO list using REST API."""
import requests
from sys import argv

link = "https://jsonplaceholder.typicode.com"

employee_id = argv[1]
employee = requests.get(f"{link}/users?id={employee_id}").json()
employee_name = employee[0]["name"]

todo_list = requests.get(f"{link}/todos?userId={employee_id}").json()
total_tasks = len(todo_list)
tasks_done = [task for task in todo_list if task["completed"] is True]

print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                       len(tasks_done),
                                                       total_tasks))

for task in tasks_done:
    print("\t ", task["title"], sep="")

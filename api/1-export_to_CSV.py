#!/usr/bin/python3
"""Returns info about an employee's TODO list using REST API."""
import requests
from sys import argv
import csv

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com"

    employee_id = argv[1]
    employee = requests.get(f"{link}/users/{employee_id}").json()
    employee_name = employee["name"]

    todo_list = requests.get(f"{link}/todos?userId={employee_id}").json()

    file_name = f"{employee_id}.csv"
    all_tasks = []
    for todo in todo_list:
        task = [todo["userId"], employee_name, todo["completed"], todo["title"]]
        all_tasks.append(task)

    with open(file_name, mode="w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)

#!/usr/bin/python3
"""Exports employee's data into a json file"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com"

    employee_id = argv[1]
    employee = requests.get(f"{link}/users/{employee_id}").json()
    employee_name = employee.get("username")

    todo_list = requests.get(f"{link}/todos?userId={employee_id}").json()

    tasks = {employee_id: [{"task": todo.get("title"),
                            "completed": todo.get("completed"),
                            "username": employee_name}
             for todo in todo_list]}

    file_name = f"{employee_id}.json"
    with open(file_name, mode="w", encoding="utf-8") as f:
        json.dump(tasks, f)

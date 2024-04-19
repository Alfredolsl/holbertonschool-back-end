#!/usr/bin/python3
"""Export employee's data into a csv file"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com"

    employee_id = int(argv[1])
    employee = requests.get(f"{link}/users/{employee_id}").json()
    employee_name = employee.get("name")

    todo_list = requests.get(f"{link}/todos?userId={employee_id}").json()

    file_name = f"{employee_id}.csv"
    all_tasks = []
    for todo in todo_list:
        task = [todo.get("userId"), employee_name,
                todo.get("completed"), todo.get("title")]
        all_tasks.append(task)

    with open(file_name, mode="w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)

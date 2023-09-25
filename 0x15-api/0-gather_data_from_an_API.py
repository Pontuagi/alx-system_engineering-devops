#!/usr/bin/python3

"""
A python script using REST API.
It takes an employee ID and returns information about their TODO list
"""

import requests
import sys


def get_employee_todo(employee_id):
    """
    A function that Return TODO list for an Employee
    The function takes one argument - employee id
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # retrieve employee information
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        employee_name = employee_data["name"]
    else:
        print("Failed to retrieve employee list information")
        return

    # Retrieve employee todo list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if todo_response.status_code == 200:
        todo_data = todo_response.json()
    else:
        print("Failed to retrieve TODO list informationi.}")
        return

    # Calculate the progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    # Display
    print("Employee {} is done with tasks({}/{}):".format(
            employee_name,
            completed_tasks,
            total_tasks)
          )

    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: 0-gather_data_from_an_API.py <employee_id>.")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo(employee_id)
        except ValueError:
            print("Employee id must be an interger.")

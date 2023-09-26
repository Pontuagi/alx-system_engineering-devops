#!/usr/bin/python3

"""
A Python script using REST API.
It takes an employee ID and returns information about their TODO list.
It exports the employee data to CSV and JSON formats.
"""

import csv
from io import StringIO
import json
import requests
import sys


def get_employee_todo(employee_id):
    """
    Return TODO list for an Employee.

    :param employee_id: The employee's ID.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Retrieve employee information
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        employee_name = employee_data["username"]
    else:
        print("Failed to retrieve employee list information.")
        return

    # Retrieve employee todo list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if todo_response.status_code == 200:
        todo_data = todo_response.json()
    else:
        print("Failed to retrieve TODO list information.")
        return

    # Create a dictionary to store task data
    tasks_dict = {employee_id: [{
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        } for task in todo_data]
    }

    # Export data to JSON
    json_file_name = f"{employee_id}.json"
    with open(json_file_name, mode='w') as json_file_write:
        json.dump(tasks_dict, json_file_write)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: 0-gather_data_from_an_API.py <employee_id>.")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo(employee_id)
        except ValueError:
            print("Employee id must be an integer.")

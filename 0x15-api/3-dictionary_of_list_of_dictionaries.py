#!/usr/bin/python3

"""
A Python script using REST API.
It retrieves TODO lists for all employees and exports the data in JSON format.
"""

import json
import requests


def get_todo_lists():
    """
    Retrieve TODO lists for all employees.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Retrieve a list of all users
    users_response = requests.get(f"{base_url}/users")
    if users_response.status_code != 200:
        print("Failed to retrieve user information.")
        return

    users_data = users_response.json()
    todo_all_employees = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        # Retrieve the TODO list for the current user
        todo_response = requests.get(f"{base_url}/todos?userId={user_id}")
        if todo_response.status_code == 200:
            todo_data = todo_response.json()
        else:
            print(f"Failed to retrieve TODO list for user {username}.")
            continue

        # Organize the task data in the specified format
        tasks = [{
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
            } for task in todo_data]

        # Add the tasks to the dictionary
        todo_all_employees[user_id] = tasks

    # Export data to JSON
    json_file_name = "todo_all_employees.json"
    with open(json_file_name, mode='w') as json_file_write:
        json.dump(todo_all_employees, json_file_write)


if __name__ == '__main__':
    get_todo_lists()

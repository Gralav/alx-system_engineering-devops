# Import requests module
import requests

# Define a function that takes an employee ID and returns their TODO list progress
def get_employee_todo_progress(employee_id):
    # Send a GET request to get user information
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")

    # Check if the request was successful
    if user_response.status_code != 200:
        raise Exception(f"User request failed with status code {user_response.status_code}")

    # Parse user data as JSON and get employee name
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Send another GET request to get TODO items for that user
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    # Check if the request was successful
    if todo_response.status_code != 200:
        raise Exception(f"TODO request failed with status code {todo_response.status_code}")

    # Parse TODO data as JSON and loop through it
    todo_data = todo_response.json()
    done_tasks = 0 # Counter for done tasks
    completed_task_titles = [] # List for completed task titles
    for item in todo_data:
        # Check if item is completed
        if item["completed"]:
            # Increment done tasks counter and append item title to list
            done_tasks += 1
            completed_task_titles.append(item["title"])

    # Get total number of tasks
    total_tasks = len(todo_data)

    # Return a dictionary with employee name and TODO list progress
    return {
        "employee_name": employee_name,
        "done_tasks": done_tasks,
        "total_tasks": total_tasks,
        "completed_task_titles": completed_task_titles
    }

# Get employee ID from user input and convert it to integer
employee_id = int(input("Enter employee ID: "))

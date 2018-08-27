#!/usr/bin/python3
"""
    This script exports todo list of a user to csv
"""
import csv
import requests
from sys import argv


def csv_functions():

    global in_csv_mode
    global write_csv

    def in_csv_mode():
        """
            determintes if csv should be created
        """
        return len(argv) > 2

    def write_csv(todos, username):
        """
            adds username to list of todos
        """
        [t["data"].update(**{"username": username}) for t in todos]
        header = ["userId", "username", "completed", "title"]
        rows = []
        for t in todos:
            new_dict = {}
            for field in header:
                new_dict[field] = t["data"].get(field)
            rows.append(new_dict)

        with open("{}.csv".format(rows[0]["userId"]),
                  "w", newline="") as csvfile:
            fields = header
            writer = csv.DictWriter(csvfile, fieldnames=fields,
                                    quoting=csv.QUOTE_ALL)

        for row in rows:
                writer.writerow(row)


def helper_functions():

    global get_uid
    global filter_by_user

    def get_uid():
        """
            Get the uid passed through cmdline
        """
        if len(argv) == 1:
            return 0
        else:
            return int(argv[1])

    def filter_by_user(datalist, uid):
        """
            filters todos belonging to user
            filters further for completed todos by that user
        """
        total = []
        for todo in datalist:
            completed = False
            if todo.get("userId") == uid:
                if todo.get("completed"):
                    completed = True
                total.append({"data": todo, "completed": completed})
        return (total)


if __name__ == "__main__":
    helper_functions()
    csv_functions()
    csv_mode = in_csv_mode()
    uid = get_uid()
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    todo_res = requests.get(todo_url)
    user_res = requests.get(user_url)
    tcode = todo_res.status_code
    ucode = user_res.status_code
    if tcode & ucode != 200:
        print("error\ntodos:{}\nusers:{}".format(tcode, ucode))
        exit(0)
    todolist = todo_res.json()
    user = user_res.json()
    todos = filter_by_user(todolist, uid)
    name = user.get("name")
    username = user.get("username")
    if not csv_mode:
        completed = [todo for todo in todos if todo.get("completed")]
        print("Employee {} is done with tasks({}/{}):".format(
            name,
            len(completed),
            len(todos))
        )
        for todo in completed:
            print("\t {}".format(todo["data"].get("title")))
    else:
        write_csv(todos, username)

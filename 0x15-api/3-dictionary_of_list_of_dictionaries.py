#!/usr/bin/python3
"""
    This script exports all todo lists to json
"""
import csv
import json
import requests
from sys import argv


def json_functions():
    """
        Functions related to json interaction
    """
    global in_json_mode
    global write_json

    def in_json_mode():
        """
            determines if json should be created
        """
        return True

    def write_json(todos, username):
        """
            writes to json file
        """
        tasks = []
        headers = [("task", "title"), ("completed", "completed"),
                   ("username", "username")]
        rows = append_username(todos, username)
        for row in rows:
            task = {}
            for attr, mapping in headers:
                task[attr] = row.get(mapping)
            tasks.append(task)
        uid = str(rows[0].get("userId"))
        output = {uid: tasks}
        # with open("{}.json".format(uid), 'w') as fs:
        #    json.dump(output, fs)
        return json.dumps(output)

def csv_functions():
    """
        Functions related to csv interaction
    """

    global in_csv_mode
    global write_csv

    def in_csv_mode():
        """
            determines if csv should be created
        """
        return False

    def write_csv(todos, username):
        """
            writes to csv file
        """
        rows = append_username(todos, username)
        header = ["userId", "username", "completed", "title"]

        with open("{}.csv".format(rows[0]["userId"]),
                  "w", newline="") as csvfile:
            fields = header
            writer = csv.DictWriter(csvfile, fieldnames=fields,
                                    quoting=csv.QUOTE_ALL)

            for row in rows:
                writer.writerow(row)


def helper_functions():
    """
        Basic stateless functions used repetitiously elsewhere
    """
    global get_uid
    global filter_by_user
    global append_username

    def append_username(todos, username):
        """
            creates a list of dictionaries
            format of each dict:
            {
                userId: id
                username: name
                title: task
                completed: boolean
            }
        """
        [t["data"].update(**{"username": username}) for t in todos]
        header = ["userId", "username", "completed", "title"]
        rows = []
        for t in todos:
            new_dict = {}
            for field in header:
                new_dict[field] = t["data"].get(field)
            rows.append(new_dict)
        return rows

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
    json_functions()
    json_mode = in_json_mode()
    csv_mode = in_csv_mode()
    #uid = get_uid()
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_res = requests.get(todo_url)
    user_res = requests.get(user_url)
    tcode = todo_res.status_code
    ucode = user_res.status_code
    if tcode & ucode != 200:
        print("error\ntodos:{}\nusers:{}".format(tcode, ucode))
        exit(0)
    todolist = todo_res.json()
    users = user_res.json()
    all_list = []
    all_dict = {}
    for user in users:
        uid = user.get('id')
        todos = filter_by_user(todolist, uid)
        name = user.get("name")
        username = user.get("username")
        all_list.append(json.loads(write_json(todos, username)))
    for obj in all_list:
        for k, v in obj.items():
            all_dict[k] = v
    with open("todo_all_employees.json", 'w') as fs:
        json.dump(all_dict, fs)

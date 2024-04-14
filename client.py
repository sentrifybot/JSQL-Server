import requests

def execute_command(command, username, password):
    url = "http://localhost:5000/"
    auth = (username, password)
    data = {"command": command}
    response = requests.post(url, json=data, auth=auth)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        return "Unauthorized: Invalid credentials."
    elif response.status_code == 400:
        return "Bad Request: Missing command."
    else:
        return "Unexpected Error."


while True:
    username = "admin"
    password = "pass"
    command = input("JSQL> ")
    result = execute_command(command, username, password)
    print(result)
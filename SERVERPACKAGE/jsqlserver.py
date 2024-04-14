import requests

class Connect:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

    def execute_command(self, command):
        auth = (self.username, self.password)
        data = {"command": command}
        response = requests.post(self.url, json=data, auth=auth)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return "Unauthorized: Invalid credentials."
        elif response.status_code == 400:
            return "Bad Request: Missing command."
        else:
            return "Unexpected Error."
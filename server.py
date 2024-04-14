from flask import Flask, request, jsonify
from jsql import JSQL

JSQL = JSQL()

app = Flask(__name__)
with open("config.txt", "r") as file:
    config = dict(line.strip().split('=') for line in file)

@app.route("/", methods=["POST"])
def execute_command():
    auth = request.authorization
    if not auth or auth.username != config["username"] or auth.password != config["password"]:
        return "Unauthorized: Invalid credentials."

    command = request.json.get("command")
    if not command:
        return "Bad Request", 400

    result = JSQL.execute_sql(command)
    return jsonify(result)
if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"])
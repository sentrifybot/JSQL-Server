from jsqlserver import Connect

client = Connect(username="admin", password="pass", url="http://localhost:5000")

result = client.execute_command("FLUSH")
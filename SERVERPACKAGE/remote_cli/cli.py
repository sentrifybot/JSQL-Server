from jsqlserver import Connect
import argparse
import sys

client = Connect(username="admin", password="pass", url="http://45.143.196.233:8000")

def process_command(command):
    """Process and execute a JSQL command."""
    result = client.execute_command(command)
    print(result)

def display_help():
    """Displays help information."""
    help_text = """
Available Commands:
    CREATE TABLE <table_name> - Creates a new table.
    INSERT INTO <table_name> VALUES <json_data> - Inserts data into a table.
    SELECT * FROM <table_name> WHERE <condition> - Queries data from a table.
    DELETE FROM <table_name> WHERE <condition> - Deletes data from a table based on a condition.
    DELETE TABLE <table_name> - Deletes an entire table from the database.
    MODIFY <table_name> SET <json_data> WHERE <condition> - Modifies data in a table based 
    FLUSH - Removes all tables from the database.
    HELP - Displays this help message.
    QUIT - Exits the CLI.
"""
    print(help_text)

def main():
    parser = argparse.ArgumentParser(description="JSQL Command Line Interface.")
    parser.add_argument('command', nargs='*', help="Optional: JSQL command to execute on startup.")
    args = parser.parse_args()

    if args.command:
        command = ' '.join(args.command)
        process_command(command)
    else:
        print("JSQL Interactive CLI. Type 'HELP' for available commands or 'QUIT' to exit.")
        while True:
            try:
                user_input = input("JSQL> ")
                if user_input.strip().upper() == "QUIT":
                    break
                elif user_input.strip().upper() == "HELP":
                    display_help()
                else:
                    process_command(user_input)
            except KeyboardInterrupt:
                print("\nExiting CLI.")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
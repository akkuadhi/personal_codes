import pyodbc


def connect_to_sql_server(server_name, database_name, username, password):
    """Connects to a SQL Server database using username and password."""
    connection_string = (
        "Driver={SQL Server};"
        f"Server={server_name};"
        f"Database={database_name};"
        f"uid={username};"
        f"pwd={password};"
    )
    connection_object = pyodbc.connect(connection_string)
    return connection_object


def connect_to_sql_server_trusted_connection(server_name, database_name):
    """Connects to a SQL Server database using a trusted connection."""
    connection_string = (
        "Driver={SQL Server};"
        f"Server={server_name};"
        f"Database={database_name};"
        "Trusted_Connection=yes;"
    )
    connection_object = pyodbc.connect(connection_string)
    return connection_object


if __name__ == "__main__":
    server_name = "localhost"
    database_name = "test_database"
    username = "sa"
    password = "password"

    connection_object = connect_to_sql_server(
        server_name=server_name,
        database_name=database_name,
        username=username,
        password=password,
    )
    print("Connected to SQL Server")

    connection_object = connect_to_sql_server_trusted_connection(
        server_name=server_name, database_name=database_name
    )
    print("Connected to SQL Server using trusted connection")

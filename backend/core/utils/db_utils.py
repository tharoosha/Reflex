from db.aiven_connection import get_connection

def execute_query(query, params=None):
    """
    Executes a query and fetches the results.
    :param query: The SQL query to execute.
    :param params: Optional query parameters for prepared statements.
    :return: Query results if applicable, or None.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params or ())
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            connection.commit()
    finally:
        connection.close()

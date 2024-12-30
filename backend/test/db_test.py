from core.utils.db_utils import execute_query

def test_database():
    # Create a table
    results = execute_query("SELECT Product_variation FROM Product WHERE Product_name = 'Milk'; ")

    # Insert data
    # execute_query("INSERT INTO test_table (value) VALUES (%s), (%s)", ("Test1", "Test2"))

    # Retrieve data
    # results = execute_query("SELECT * FROM test_table")
    print("Data in test_table:", results)



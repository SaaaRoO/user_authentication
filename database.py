import psycopg2  # Import psycopg2 for PostgreSQL interaction
from psycopg2.extras import RealDictCursor  # Import RealDictCursor for returning query results as dictionaries
from config import Config  # Import configuration settings

def get_db_connection():
    """
    Establish a connection to the PostgreSQL database using the URI in Config.
    """
    conn = psycopg2.connect(Config.DATABASE_URI)  # Connect to the database using Config settings
    return conn

def query_db(query, args=(), one=False):
    """
    Execute a query in the database and return results.

    Parameters:
    - query: SQL query to execute
    - args: Tuple of arguments for parameterized queries
    - one: Boolean indicating whether to fetch one or all results
    """
    conn = get_db_connection()  # Get a connection to the database
    cursor = conn.cursor(cursor_factory=RealDictCursor)  # Create a cursor with RealDictCursor for dict-like row access
    cursor.execute(query, args)  # Execute the query with provided arguments
    result = cursor.fetchall()  # Fetch all results
    conn.commit()  # Commit transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the connection
    return (result[0] if result else None) if one else result  # Return a single result or all results

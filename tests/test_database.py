from database import get_db_connection


def test_database_connection():
    conn = get_db_connection()
    assert conn is not None
    conn.close()


def test_insert_and_query():
    conn = get_db_connection()
    cur = conn.cursor()

    # Insert test record
    cur.execute("INSERT INTO records (name, age) VALUES (%s, %s) RETURNING id;", ("Test", 25))
    conn.commit()

    # Query record
    cur.execute("SELECT name, age FROM records WHERE name = %s;", ("Test",))
    result = cur.fetchone()

    assert result == ("Test", 25)

    cur.close()
    conn.close()

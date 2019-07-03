import psycopg2


def deleteInBulk():
    try:
        ps_connection = psycopg2.connect(user="postgres",
                                         password="postgres",
                                         host="127.0.0.1",
                                         port="5432",
                                         database="ostadkar")
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE cities cascade;")
        ps_connection.commit()
        row_count = cursor.rowcount
        print(row_count, "Record Deleted")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")


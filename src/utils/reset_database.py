from dao.db_connection import DBConnection
from utils.sql_utils import execute_sql_file


def reset_database():
    with DBConnection().connection as connection:
        with connection.cursor() as cursor:
            queries = [
                "DELETE FROM have;",
                "DELETE FROM favorites;",
                "DELETE FROM users;",
                "ALTER SEQUENCE users_id_user_seq RESTART WITH 1;",
            ]
            for query in queries:
                cursor.execute(query)
    execute_sql_file("data/data_insert.sql")


if __name__ == "__main__":
    reset_database()

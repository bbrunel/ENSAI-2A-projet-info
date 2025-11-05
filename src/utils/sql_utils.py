from dao.db_connection import DBConnection

def execute_sql_file(filename: str):
    with open(filename, "r") as f:
        init_script = f.read()
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                for statement in init_script.split(";"):
                    stmt = statement.replace('\n','')
                    stmt = stmt.replace('\t','')
                    if stmt:
                        cursor.execute(stmt + ';')


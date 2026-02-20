from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Subject:
    __scripts = {
        "insert": text("INSERT INTO subject(subject_id, subject_title) "
                       "VALUES (:id, :title)"),
        "delete": text("DELETE FROM subject WHERE subject_id = :id"),
        "update": text("UPDATE subject SET subject_title = :title "
                       "WHERE subject_id = :id"),
        "select": text("SELECT * FROM subject WHERE subject_id = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def insert(self,  new_id, title):
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["delete"], {"id": new_id})
            conn.execute(self.__scripts["insert"],
                         {"id": new_id, "title": title})
            conn.commit()
            result = conn.execute(self.__scripts["select"],
                                  {"id": new_id})
            return result.mappings().all()

    def update(self, new_id, title):
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["update"],
                         {"id": new_id, "title": title})
            conn.commit()
            result = conn.execute(self.__scripts["select"], {"id": new_id})
            return result.mappings().all()

    def delete(self, new_id):
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["delete"], {"id": new_id})
            conn.commit()
            res = conn.execute(self.__scripts["select"], {"id": new_id})
            return res.mappings().all()

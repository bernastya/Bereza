from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:jY1sebeq@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_full_subject():
    new_id = 100
    sql_insert = text("INSERT INTO subject(subject_id, subject_title \
                      ) VALUES (:id, :title)")
    sql_delete = text("DELETE FROM subject WHERE subject_id = :id")
    sql_update = text("UPDATE subject SET subject_title = :title  \
                      WHERE subject_id = :id")
    sql_select = text("SELECT * FROM subject WHERE subject_id = :id")

    with db.connect() as conn:
        conn.execute(sql_delete, {"id": new_id})
        conn.commit()
        result = conn.execute(sql_select, {"id": new_id}).mappings().all()
        assert len(result) == 0

        conn.execute(sql_insert, {"id": new_id, "title": "biology"})
        conn.commit()
        result = conn.execute(sql_select, {"id": new_id}).mappings().one()
        assert result["subject_title"] == "biology"

        conn.execute(sql_update, {"id": new_id, "title": "zoology"})
        conn.commit()
        result = conn.execute(sql_select, {"id": new_id}).mappings().one()
        assert result["subject_title"] == "zoology"

        conn.execute(sql_delete, {"id": new_id})
        conn.commit()
        result = conn.execute(sql_select, {"id": new_id}).mappings().all()
        assert len(result) == 0

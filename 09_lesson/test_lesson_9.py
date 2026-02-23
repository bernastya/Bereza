from subject import Subject

db_connection_string = "postgresql://postgres:jY1sebeq@localhost:5432/QA"
base = Subject(db_connection_string)


def test_insert_subject():
    test_id = 100
    title = "biology"
    result = base.insert(test_id, title)
    assert result[0]["subject_title"] == title
    base.delete(test_id)


def test_update():
    test_id = 200
    title = "biology"
    new_title = "zoology"
    base.insert(test_id, title)
    result = base.update(test_id, new_title)
    assert result[0]["subject_title"] == new_title
    base.delete(test_id)


def test_delete():
    test_id = 300
    title = "biology"
    base.insert(test_id, title)
    result = base.delete(test_id)
    assert len(result) == 0

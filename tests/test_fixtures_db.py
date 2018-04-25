import sqlite3
import pytest


@pytest.fixture()
def db(log):
    # setup
    logger = log.getChild("db")
    conn = sqlite3.connect(":memory:")
    conn.set_trace_callback(logger.debug)
    # /setup

    yield conn

    # teardown
    conn.close()
    # /teardown


@pytest.fixture()
def testtable(db):
    create_stmt = "CREATE TABLE testtable (i INTEGER PRIMARY KEY , col1, col2)"

    db.execute(create_stmt)
    db.commit()

    return db


@pytest.mark.db  # invoke: pytest -m db -o log_cli=true
@pytest.mark.parametrize("data", (
        (1, "foo", "bar"),
        (2, "bla", "blubb")
), ids=["foobar", "blablubb"])
def test_db(testtable, log, data):
    log.info("starting test")

    cur = testtable.cursor()
    insert_stmt = "INSERT INTO testtable VALUES (?, ?, ?)"
    select_stmt = "SELECT i, col1, col2 from testtable"

    cur.execute(insert_stmt, data)
    cur.execute(select_stmt)
    row = cur.fetchone()
    assert row == data

    log.info("test done")

import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text


engine = create_engine(
    "mysql+mysqldb://{0}:{1}@{2}:{3}/{4}".format(
        "mainuser", "mainpass", "mysql", 3306, "maindb"
    )
)

metadata = MetaData()
books = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(32), nullable=False, default=""),
    Column("primary_author", String(32), nullable=False, default=""),
)

metadata.create_all(engine)

inspector = inspect(engine)
print(inspector.get_columns("book"))


with engine.connect() as con:

    data = (
        {"title": "The Hobbit", "primary_author": "Tolkien"},
        {"title": "The Silmarillion", "primary_author": "Tolkien"},
    )

    statement = text(
        """INSERT INTO book(title, primary_author) VALUES(:title, :primary_author)"""
    )

    for line in data:
        con.execute(statement, **line)


with engine.connect() as con:

    rs = con.execute("SELECT * FROM book")

    for row in rs:
        print(row)
import sqlalchemy

from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Text

from sqlalchemy.sql import text

engine = create_engine(
    "mysql+mysqldb://{0}:{1}@{2}:{3}/{4}".format(
        "mainuser", "mainpass", "mysql", 3306, "maindb"
    )
)

metadata = MetaData()

books = Table(
    "book2",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(32), nullable=False, default=""),
    Column("primary_author", String(32), nullable=False, default=""),
)


tweets = Table(
    "tweets",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tweet_id", Text, nullable=False, default=""),
    Column("created_at", Text, nullable=False, default=""),
)


metadata.create_all(engine)
inspector = inspect(engine)
print(inspector.get_columns("book2"))

with engine.connect() as con:

    data = (
        {"title": "The Hobbit", "primary_author": "Tolkien"},
        {"title": "The Silmarillion", "primary_author": "Tolkien"},
    )

    # statement = text(
    #     """INSERT INTO book(title, primary_author) VALUES(:title, :primary_author)"""
    # )

    statement = lambda x: text(
        """INSERT INTO {}({}) VALUES(:{})""".format(
            "book2", ",  ".join(x), ", :".join(x)
        )
    )

    for line in data:
        con.execute(statement(line), **line)


with engine.connect() as con:

    rs = con.execute("SELECT * FROM book2")

    for row in rs:
        print(row)
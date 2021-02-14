import sqlalchemy

from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, BigInteger, DateTime, MetaData, Text

from sqlalchemy.sql import text

engine = create_engine(
    "mysql+mysqldb://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(
        "mainuser", "mainpass", "mysql", 3306, "maindb"
    )
)

metadata = MetaData()

tweets = Table(
    "tweets",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("tweet_id", BigInteger, nullable=True, default=""),
    Column("created_at", DateTime, nullable=True, default=""),
    Column("text", Text, nullable=True, default=""),
    Column("hashtags", Text, nullable=True, default=""),
    Column("url", Text, nullable=True, default=""),
    Column("expanded_url", Text, nullable=True, default=""),
    Column("display_url", Text, nullable=True, default=""),
    Column("source", Text, nullable=True, default=""),
    Column("user_id", BigInteger, nullable=True, default=""),
    Column("name", Text, nullable=True, default=""),
    Column("screen_name", Text, nullable=True, default=""),
    Column("location", Text, nullable=True, default=""),
    Column("description", Text, nullable=True, default=""),
    Column("followers_count", Integer, nullable=True, default=""),
    Column("friends_count", Integer, nullable=True, default=""),
    Column("listed_count", Integer, nullable=True, default=""),
    Column("favourites_count", Integer, nullable=True, default=""),
    Column("statuses_count", Integer, nullable=True, default=""),
    Column("geo", Text, nullable=True, default=""),
    Column("coordinates", Text, nullable=True, default=""),
    Column("contributors", Text, nullable=True, default=""),
    Column("retweet_count", Text, nullable=True, default=""),
    Column("favorite_count", Text, nullable=True, default=""),
    Column("lang", Text, nullable=True, default=""),
    Column("keyword", Text, nullable=True, default=""),
)


metadata.create_all(engine)
inspector = inspect(engine)


def insert_json_data(data, db):
    with engine.connect() as con:

        statement = lambda x: text(
            """INSERT INTO {}({}) VALUES(:{})""".format(
                db, ",  ".join(x), ", :".join(x)
            )
        )

        con.execute(statement(data), **data)
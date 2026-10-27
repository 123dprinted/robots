from dotenv import load_dotenv
import sqlite3
import os
load_dotenv()
db = sqlite3.connect(os.getenv("DATABASE"))
cursor = db.cursor()

print("DB successfully connected.")

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS Messages (
MessageID INTEGER PRIMARY KEY,
ChannelID INTEGER,
AuthorID INTEGER,
ReplyID INTEGER NULL,
Content TEXT,
Timestamp INTEGER
);


"""

cursor.execute(CREATE_TABLE_QUERY)

def add_message(id, author_id, channel_id, reply_id, content, time):
    cursor.execute(
        "INSERT INTO Messages (MessageID, ChannelID, AuthorID, ReplyID, Content, Timestamp)"
        "VALUES (?, ?, ?, ?, ?, ?)",
        (id, author_id, channel_id,
         reply_id if reply_id else None,
         content, time,
    ))


    print("Successfully added message.")

def commit():
    db.commit()
    print("Successfully committed.")


def close():
    db.commit()
    db.close()
    print("Successfully closed db.")


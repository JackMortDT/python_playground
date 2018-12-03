import uuid
import datetime
from database import Database

class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
                "id": self.id,
                "blog_id": self.blog_id,
                "title": self.title,
                "content": self.content,
                "author": self.author,
                "date_created": self.date_created
                }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts', query={"id": id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={"blog_id": id})]

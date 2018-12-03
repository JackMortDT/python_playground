import uuid
import datetime
from database import Database
from models.post import Post

class Blog(object):

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave black for today (in format DDMMYYYY): ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.strptime(date, "%d%m%Y"))
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
                "id": self.id,
                "author": self.author,
                "title": self.title,
                "description": self.description
                }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Databa.find_one(collection="blogs",
                                    query={'id': id})
        return cls(id=blog_data['id'],
                    author=blog_data['author',
                    title=blog_data['title'],
                    description=blog_data['description'])
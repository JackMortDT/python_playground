from database import Database
from models.post import Post

Database.initialize()

post = Post("Title", "Content", "Author")

print(post.title)

# services/post_service.py
from blog.repositories.post_repository import PostRepository

class PostService:
    def __init__(self):
        self.post_repository = PostRepository()

    def list_posts(self):
        return self.post_repository.get_all_posts()
    
    def get_post_by_id(self, post_id):
        return self.post_repository.get_post_by_id(post_id)

    def create_post(self, title, content, author, category):
        return self.post_repository.create_post(title, content, author, category)

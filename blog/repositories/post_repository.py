# repositories/post_repository.py

from blog.models.post import Post


class PostRepository:
    def get_all_posts(self):
        return Post.objects.all()

    def get_post_by_id(self, post_id):
        return Post.objects.get(id=post_id)

    def create_post(self, title, content, author, category):
        return Post.objects.create(title=title, content=content, author=author, category=category)

# services/category_service.py
from blog.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def list_categories(self):
        return self.category_repository.get_all_categories()

    def create_category(self, name):
        return self.category_repository.create_category(name)

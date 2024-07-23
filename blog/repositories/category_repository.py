# repositories/category_repository.py

from blog.models.category import Category


class CategoryRepository:
    def get_all_categories(self):
        return Category.objects.all()

    def get_category_by_id(self, category_id):
        return Category.objects.get(id=category_id)

    def create_category(self, name):
        return Category.objects.create(name=name)

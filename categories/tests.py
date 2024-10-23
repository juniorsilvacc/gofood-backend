from django.test import TestCase
from django.urls import reverse
from categories.models import Category


class CategoryListViewTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Pizzas')
        Category.objects.create(name='Burguers')

    def test_list_view_status_code(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('categories'))
        self.assertTemplateUsed(response, 'categories/categories.html')

    def test_list_view_content(self):
        response = self.client.get(reverse('categories'))
        self.assertContains(response, "Pizzas")
        self.assertContains(response, "Burguers")

    def test_search_filter(self):
        response = self.client.get(reverse('categories') + '?name=Pizzas')
        self.assertContains(response, "Pizzas")
        self.assertNotContains(response, "Burguers")


class CategoryCreateViewTest(TestCase):
    def test_create_category(self):
        response = self.client.post(reverse('category_create'), {
            'name': 'Pizzas'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='Pizzas').exists())


class CategoryDetailViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Pizzas")

    def test_detail_view(self):
        response = self.client.get(reverse('category_detail', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizzas")


class CategoryUpdateViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Pizzas")

    def test_update_category(self):
        response = self.client.post(reverse('category_update', kwargs={'pk': self.category.pk}), {
            'name': 'Burguers'
        })
        self.assertEqual(response.status_code, 302)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Burguers')


class CategoryDeleteViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Sucos")

    def test_delete_category(self):
        response = self.client.post(reverse('category_delete', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Category.objects.filter(pk=self.category.pk).exists())
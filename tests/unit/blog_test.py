from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        #self.assertEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Author')

        self.assertEqual(b.__repr__(), 'Test por Test Author (0 posts)')

    def  test_day(self):
        b2 = Blog('My Day', 'Edson')

        self.assertEqual(b2.__day__(), 'My Day by Edson (2 posts)')

    
class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = ['asd', 12]

    def __repr__(self):
        return 'Test por Test Author (0 posts)'

    def __day__(self):
        pt = 'posts' if (len(self.posts) > 1)  else 'post';
        return '{} by {} ({} {})'.format(self.title, self.author, len(self.posts), pt )
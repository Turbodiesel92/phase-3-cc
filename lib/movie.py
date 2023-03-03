class Movie:

    def __init__(self, title):
        self.title = title

        self.reviews = []
        self.reviewers = []

    def get_title(self):
        return self._title

    def set_title(self, title):
        if type(title) == str and (len(title) > 0):
            self._title = title
        else:
            print("Titles must be strings greater than 0 characters")

            raise Exception("Titles must be strings greater than 0 characters")

    title = property(get_title, set_title)

    def average_rating(self):
        total = 0

        for rating in self.reviews:
            total += rating

        average = total / len(self.reviews)

        return average










    @classmethod
    def highest_rated(cls):
        return cls.reviews.limit

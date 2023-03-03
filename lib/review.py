from movie import Movie
from viewer import Viewer

class Review:

    def __init__(self, rating, viewer, movie):
        self.rating = rating
        self.viewer = viewer
        self.movie = movie

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewer is not an instance of class Viewer")

    # @property
    def get_movie(self):
        return self._movie

    # @movie.setter
    def set_movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("Movie is not an instance of class Movie")

    movie = property(get_movie, set_movie)




    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if type(rating) == int and (rating > 0 and rating < 6):
            self._rating = rating
        else:
            print("Ratings must be integers between 1 and 5.")

            raise Exception("Ratings must be integers between 1 and 5.")







# Review
# Review __init__(self, viewer, movie, rating)
# Review is initialized with a Viewer instance, a Movie instance, and a rating (number)
# Review property rating()
# Returns the rating for the Review instance
# Ratings must be integers between 1 and 5, inclusive



# Review property viewer()
# Returns the viewer who wrote the review
# Viewers must be Viewer instances
# You will need to import Viewer inside of this property to avoid a circular import.
# Review property movie()
# Returns the movie that is being reviewed
# Movies must be Movie instances
# You will need to import Movie inside of this property to avoid a circular import.
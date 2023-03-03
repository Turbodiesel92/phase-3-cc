from movie import Movie
from viewer import Viewer

class Review:

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

    @property
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("This sucks")





    # rating property goes here!

    # viewer property goes here!

    # movie property goes here!

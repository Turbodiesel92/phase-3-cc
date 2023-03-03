class Viewer:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self._username

    def set_username(self, username):
        if type(username) == str and (len(username) > 6 and len(username) < 16):
            self._username = username
        else:
            raise Exception("Usernames must be unique strings between 6 and 16 characters, inclusive")

    username = property(get_username, set_username)








    def reviewed_movie(self, movie):

        pass

    def rate_movie(self, movie, rating):
        from review import Review
        Review(self, movie, rating)





# Viewer
# Viewer reviews
# Returns a list of Review instances associated with the Viewer instance.
# Viewer reviewed_movies
# Returns a list of Movie instances reviewed by the Viewer instance.
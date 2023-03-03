class Viewer:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self._get_username

    def set_username(self, username):
        if type (username) == str and (len(username) > 6 and len(username) < 16):
            self._username = username
        else:
            raise Exception("Usernames must be unique strings between 6 and 16 characters, inclusive")

    username = property(get_username, set_username)








    def reviewed_movie(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass




from .DELETE_MOVIES.delete_movies import DeleteMovies
from .GET_MOVIES.get_movies import GetMovies
from .PATH_MOVIES.path_movies import PatchMovies
from .POST_MOVIES.post_movies import PostMovies
from .admin_auth import AdminAuth

class ApiManager:
    def __init__(self, session) :
        self.session = session
        self.api_get_movies = GetMovies(session)
        self.api_post_movies = PostMovies(session)
        self.api_delete_movies = DeleteMovies(session)
        self.api_patch_movies = PatchMovies(session)
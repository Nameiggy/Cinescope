from Movies.constans import ENDPOINT
from Movies.custrim_request.CostomRequest import CustomRequester


class PostMovies (CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url="https://api.dev-cinescope.coconutqa.ru")



    def post_movies (self,created_movies,expected_status = 201):

        return self.send_request(
            method="POST",
            endpoint=ENDPOINT,
            data=created_movies,
            expected_status=expected_status

        )
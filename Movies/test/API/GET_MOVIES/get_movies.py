from Movies.constans import ENDPOINT
from Movies.custrim_request.CostomRequest import CustomRequester


class GetMovies (CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url="https://api.dev-cinescope.coconutqa.ru")




    def get_movies (self,params=None, expected_status = 200):


        return self.send_request(
         method = "GET",
         endpoint= ENDPOINT,
         params=params,
         expected_status=expected_status,

        )
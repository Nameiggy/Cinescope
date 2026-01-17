from Movies.constans import ENDPOINT,ENDPOINT_PATCH
from Movies.custrim_request.CostomRequest import CustomRequester


class PatchMovies (CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url="https://api.dev-cinescope.coconutqa.ru")



    def patch_movie (self,patch_movie,expected_status = 200):

        return self.send_request(
            method="PATCH",
            endpoint=ENDPOINT_PATCH,
            data=patch_movie,
            expected_status=expected_status

        )
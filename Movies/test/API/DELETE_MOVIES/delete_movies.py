from Movies.constans import ENDPOINT
from Movies.custrim_request.CostomRequest import CustomRequester


class DeleteMovies (CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url="https://api.dev-cinescope.coconutqa.ru")



    def delete_movies (self,movie_id, expected_status = 200) :
        endpoint = f"/{ENDPOINT}/{movie_id}"
        return self.send_request(
                method="DELETE",
                endpoint=endpoint,
                expected_status=expected_status
            )
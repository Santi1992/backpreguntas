from domain.entities.GenericRequest import GenericRequest
class GenericRequestParser():

    def parse_request(self, request):

        args = request.args
        headers = request.headers
        json = request.json
        #request.get_json(force=True)
        
        return GenericRequest(
            ).set_body(json
            ).set_headers(headers
            ).set_args(args
            ).set_token(
                headers.get("authorization", None)
            )
            
            


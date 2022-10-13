import logging
import azure.functions as func


"""
curl -X POST -H "Content-type: application/json" -d "{\"name\" : \"Lemons\", \"password\" : \"azure\", \"id\" : \"12\", \"recieved\" : \"1\", \"shipped\" : \"2\", \"returned\" : \"1\', \"onHan\" : \"23\"}" "https://famicy.azurewebsites.net/api/item/create"
"""
def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    password = req.route_params.get('password')
    name = req.route_params.get('name')
    id = req.route_params.get('id')
    num_recieved = req.route_params.get('recieved')
    num_shipped = req.route_params.get('shipped')
    num_returned = req.route_params.get('returned')
    num_on_hand = req.route_params.get('onHand')

    print(password,name,id,num_recieved,num_shipped,num_returned,num_on_hand)

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            print(req)
            pass
        else:
            password = req_body.get('password')
            name = req_body.get('name')
            id = req_body.get('id')
            num_recieved = req_body.get('recieved')
            num_shipped = req_body.get('shipped')
            num_returned = req_body.get('returned')
            num_on_hand = req_body.get('onHand')
        
    print(password, name, id, num_recieved, num_shipped, num_returned, num_on_hand)

    if password != 'azure':
        return func.HttpResponse("You do not have access to this resource", status_code=403)

    if name and id and num_recieved and num_shipped and num_returned and num_on_hand:
        newdocs = func.DocumentList() 
        newproduct_dict = {
            "id": id,
            "name": name,
            "recieved": num_recieved,
            "shipped": num_shipped,
            "returned": num_returned,
            "onHand": num_on_hand
        }
        newdocs.append(func.Document.from_dict(newproduct_dict))
        doc.set(newdocs)
        
        return func.HttpResponse(f"Item successfully processed!", status_code=200)
    else:
        return func.HttpResponse(
            "Missing parameters, please make sure you have provided the following fields: name, id, recieved, shipped, returned, onHand", 
             status_code=422
        )
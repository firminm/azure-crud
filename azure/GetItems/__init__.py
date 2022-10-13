import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')

    password = req.route_params.get('password')
    if password != 'azure':
        return func.HttpResponse("You do not have access to this resource", status_code=403)
 
    items_json = []
    for item in doc:
        try:
            user_json = {
            "id": item['id'],
            "name": item['name'],
            "qty_recieved": item['recieved'],
            'qty_shipped': item['shipped'],
            'qty_returned': item['returned'],
            'qty_on_hand': item['onHand']
            }
            items_json.append(user_json)
        except KeyError:
            name = item['name']
            print(f'keyerror on name={name}')

    return func.HttpResponse(
            json.dumps(items_json),
            status_code=200,
            mimetype="application/json"            
    )
from core.models import Client
from core.service import aws_svc
import hashlib
import time

def add_client(firstname, lastname, email, document):
    document_path = save_document(document, firstname, lastname)
    client = Client(firstname=firstname, lastname=lastname, email=email, document=document_path)
    client.save()
    return client.to_dict_json()

def list_clients():
    clients = Client.objects.all()
    return [client.to_dict_json() for client in clients]

def client_by_id(id):
    client = Client.objects.get(id=id)
    return client

def save_document(document, firstname, lastname):
    string_to_hash = (firstname.lower() +'_'+ lastname.lower() + ':' + str(time.time())).encode()
    document_path_name = hashlib.md5(string_to_hash).hexdigest()
    document_path = './frontend/static/documents/'+ document_path_name +'.jpeg'
    document_url = '/documents/'+ document_path_name +'.jpeg' 
    destination = open( document_path, 'wb' )
    for chunk in document.chunks():
            destination.write(chunk)
    destination.close()
    return document_url
    
def compare_photos(client_photo, client_document):
    return {
        'data': aws_svc.faces_comparation(client_photo, client_document)
    }

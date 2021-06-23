from core.models import Client
from core.service import aws_svc
import hashlib

def add_client(firstname, lastname, email, document):
    document_path = save_document(document, firstname, lastname)
    client = Client(firstname=firstname, lastname=lastname, email=email, document=document_path)
    client.save()
    return client.to_dict_json()

def list_clients():
    clients = Client.objects.all()
    return [client.to_dict_json() for client in clients]

def save_document(document, firstname, lastname):
    document_path = './frontend/static/documents/'+ firstname.lower() +'_'+ lastname.lower() +'.jpeg'
    document_url = '/documents/'+ firstname.lower() +'_'+ lastname.lower() +'.jpeg' 
    destination = open( document_path, 'wb' )
    for chunk in document.chunks():
            destination.write(chunk)
    destination.close()
    return document_url
    
def compare_photos(client_photo):
    return {
        'data': aws_svc.faces_comparation(client_photo, '')
    }

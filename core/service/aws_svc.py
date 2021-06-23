import boto3

def faces_comparation(client_photo, document_photo):
    client = boto3.client('rekognition', region_name='us-east-1')
    similarity = 0
   
    # imageSource=open('/app/frontend/static/documents/face_test.jpg','rb')
    imageSource = client_photo
    imageTarget=open('./frontend/static' + document_photo,'rb')

    response=client.compare_faces(SimilarityThreshold=90,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    
    for faceMatch in response['FaceMatches']:
        similarity = str(faceMatch['Similarity'])

    imageSource.close()
    imageTarget.close()     
    return similarity

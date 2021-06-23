import boto3

def faces_comparation(client_photo, document_photo):
    client = boto3.client('rekognition', region_name='us-east-1')
    confidence = 0
   
    # imageSource=open('/app/frontend/static/documents/face_test.jpg','rb')
    imageSource = client_photo
    imageTarget=open('/app/frontend/static/documents/levi_costa.jpeg','rb')

    response=client.compare_faces(SimilarityThreshold=90,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        confidence = similarity
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    # confidence = response['SourceImageFace']['Confidence']

    imageSource.close()
    imageTarget.close()     
    return confidence

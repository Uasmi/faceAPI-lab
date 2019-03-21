#python 3.7.2
import numpy as np
import cv2
import requests
import json
import time
from azure.storage.blob import BlockBlobService
from PIL import Image
from io import BytesIO
import keys

subscription_key = keys.subscription_key
blobAccountKey = keys.blobAccountKey
blob_service = BlockBlobService('recruitlab', blobAccountKey)
vision_base_url = "https://southcentralus.api.cognitive.microsoft.com/face/v1.0/"
assert subscription_key
#-----------------------------------------------------------------#

# API Calls to Face API
#-----------------------------------------------------------------#
def detect(imgstr):
    analyze_url = vision_base_url + "detect"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params  = {'faceId': 'True'}

    #API Call
    response = requests.post(analyze_url, headers=headers, params=params, data=imgstr)
    response.raise_for_status()
    # json with data
    analysis = response.json()
   
    try:
        faceId = analysis[0]['faceId']
    except:
        faceId = 'No Face'
    return faceId

def findSimilarFace(faceIdStr):
    analyze_url = vision_base_url + "findsimilars"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/json'}
    body  = {'faceId': str(faceIdStr),
            "faceListId": "lab-list",
            "maxNumOfCandidatesReturned": 10,
            "mode": "matchPerson"}

    #API Call
    response = requests.post(analyze_url, headers=headers, json=body)
    response.raise_for_status()
    # json with data
    analysis = response.json()
    try:
        persFaceId = analysis[0]['persistedFaceId']
        confidence = analysis[0]['confidence']
    except:
        persFaceId = ''
        confidence = "0"
    return persFaceId, confidence

def storeFace(imgstr):
    analyze_url = vision_base_url + "facelists/lab-list/persistedFaces"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params  = {}

    #API Call
    response = requests.post(analyze_url, headers=headers, params=params, data=imgstr)
    response.raise_for_status()
    # json with data
    analysis = response.json()
    return analysis

#No need to call, already done
#-----------------------------------------------------------------#
def makeFaceList():
    
    analyze_url = vision_base_url + "facelists/"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/json'}
    params  = {'faceListId': 'lab-face-list'}
    body = {'name': 'sample-face-list'}

    #API Call
    response = requests.put(analyze_url, headers=headers, params=params, data=body)
    response.raise_for_status()
    # json with data
    analysis = response.json()
    return analysis, response.elapsed.total_seconds()
#-----------------------------------------------------------------#


#Check available lists
def verifyLists():
    analyze_url = vision_base_url + "facelists/"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params  = {}
    #API Call
    response = requests.get(analyze_url, headers=headers, params=params)
    response.raise_for_status()
    # json with data
    analysis = response.json()
    return analysis, response.elapsed.total_seconds()
#-----------------------------------------------------------------#

# Main method to capture image from webcam
#-----------------------------------------------------------------#
def getImage():
    cap = cv2.VideoCapture(0)
    cap.open(0)
    ret, frame = cap.read(0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('',gray)
    cv2.waitKey(10)
    if ret is None:
        print ('no access') 
    cap.release()
    imgstr = cv2.imencode(".jpg",gray)[1].tostring()
    return imgstr
#-----------------------------------------------------------------#

# Blob storage method to store image as bytes
#-----------------------------------------------------------------#
def storeToBlob(imageLink, stored):
    name = str(stored)
    response = requests.get(imageLink)
    img = BytesIO(response.content)
    img = img.getvalue()
    print(img)
    if blob_service.exists('recruitlabblob', name) == False:
        blob_service.create_blob_from_bytes('recruitlabblob', name, img)
    else: 
        print('File already exists, do you want to overwrite?')
        key = input('y(yes), n(no)')
        if key == 'y':
            blob_service.create_blob_from_bytes('recruitlabblob', name, img)
#-----------------------------------------------------------------#


# To clean Face List run this fuction
#-----------------------------------------------------------------#
def CleanFacesInList():
    getfaces_url = vision_base_url + "facelists/lab-list"
    analyze_url = vision_base_url + "facelists/lab-list/persistedFaces/"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params  = {}
    response = requests.get(getfaces_url, headers=headers)
    response.raise_for_status
    faceList = response.json()
    faceList = faceList['persistedFaces']
    for each in faceList:
        try:
            new_url = analyze_url + str(each['persistedFaceId'])
            response = requests.delete(new_url, headers=headers)
            response.raise_for_status()
            print (response)
        except:
            continue
        
    #API Call
    response = requests.get(getfaces_url, headers=headers)
    response.raise_for_status
    faceList = response.json()
    print(faceList)
    #response.raise_for_status()
    # json with data
    #analysis = response.json()
    input("Deleted faces")
#-----------------------------------------------------------------#

# Uncomment this section to cleanup face list
#-----------------------------------------------------------------#

#CleanFacesInList()




#-----------------------------------------------------------------#

# Main
#-----------------------------------------------------------------#

print (verifyLists())
print ('Want to add your face to library?')

while True:
    key = input('y(yes),n(no):')
    if key == 'y':
        image = getImage()
        print (image)
        while True:
            try:
                stored = storeFace(image)
                stored = stored['persistedFaceId']
                print ('Your Face Id:', stored)
                print ('Please paste image URL for advertising image to include:')
                break
            except:
                print ("Something wrong with the image snapshot (no face detected, poor light), try again")
                time.sleep(5)
        # Download an image, rename it to the 
        while True:
            key = input('url here:')
            try:
                storeToBlob(key, stored)
                break
            except:
                print ('Error with the link')
        break
    elif key == 'n':
        break
    else:
        print ('Wrong input')

window = cv2.namedWindow('Advertise', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Advertise",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:
    image = getImage()
    faceIdStr = detect(image)
    print (faceIdStr)
    if faceIdStr != 'No Face':
        verify = findSimilarFace(faceIdStr)
        print (verify)
        if verify[1] > 0.5:
            advertisingImages = list(blob_service.list_blob_names('recruitlabblob'))
            for each in advertisingImages:
                print (each, verify[0])
                if each == verify[0]:
                    img = blob_service.get_blob_to_bytes('recruitlabblob', each)
                    img = BytesIO(img.content).getvalue()
                    img = np.fromstring(img, np.uint8)
                    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                    cv2.imshow('Advertise', img)
                    cv2.waitKey(100)
                    break
        else:
            img = cv2.imread('idle.jpg')
            cv2.imshow('Advertise', img)
            cv2.waitKey(10)
    else:
            img = cv2.imread('idle.jpg')
            cv2.imshow('Advertise', img)
            cv2.waitKey(10)
    time.sleep(5)



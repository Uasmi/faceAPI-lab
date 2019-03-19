#python 3.7.2
import numpy as np
import cv2
import requests
import json
#import tkinter

subscription_key = "ae56704bd8a7489dbbfa2f6c583d5f87"
assert subscription_key

def detect(imgstr):
    #API parameters
    vision_base_url = "https://southcentralus.api.cognitive.microsoft.com/face/v1.0/"
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
    #API parameters
    vision_base_url = "https://southcentralus.api.cognitive.microsoft.com/face/v1.0/"
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
    vision_base_url = "https://southcentralus.api.cognitive.microsoft.com/face/v1.0/"

    analyze_url = vision_base_url + "facelists/lab-list/persistedFaces"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params  = {}

    #API Call
    response = requests.post(analyze_url, headers=headers, params=params, data=imgstr)
    response.raise_for_status()
    # json with data
    analysis = response.json()
    return analysis, response.elapsed.total_seconds()

#No need to call, already done
def makeFaceList():
    #API parameters
    vision_base_url = "https://southcentralus.api.cognitive.microsoft.com/face/v1.0/"

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

#Check available lists
def verifyLists():
    vision_base_url = "https://southcentralus.api.cognitive.microsoft.com/face/v1.0/"
    analyze_url = vision_base_url + "facelists/"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params  = {}
    #API Call
    response = requests.get(analyze_url, headers=headers, params=params)
    response.raise_for_status()
    # json with data
    analysis = response.json()
    return analysis, response.elapsed.total_seconds()

def getImage():
    cap = cv2.VideoCapture(0)
    cap.open(0)
    ret, frame = cap.read(0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret is None:
        print ('no access') 
    cap.release()
    imgstr = cv2.imencode(".jpg",gray)[1].tostring()
    return imgstr

print (verifyLists())

print ('Want to add your face to library?')

while True:
    key = input('y(yes),n(no):')
    if key == 'y':
        #print ('Please add advertising image url from blob to include:')

        image = getImage()
        stored = storeFace(image)
        print (stored)
        
        break
    elif key == 'n':
        break
    else:
        print ('Wrong input')

image = getImage()
faceIdStr = detect(image)
print (faceIdStr)
if faceIdStr != 'No Face':
    verify = findSimilarFace(faceIdStr)
    if verify[1] > 0.5:
        if verify[0] == 'ad898e4f-a357-4c3b-8760-743e57978eb3':
            img = cv2.imread('test.jpg')
            cv2.imshow('image', img)
            cv2.waitKey(0)
    print (verify)
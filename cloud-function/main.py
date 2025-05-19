import base64
import json
import os
from flask import Flask, request
from google.cloud import aiplatform

PROJECT = "fleet-monitoring-project"
REGION = "us-central1"
ENDPOINT_ID = "8626615399414235136"  # your Vertex AI endpoint ID

def predict_vehicle_failure(event, context):
    # Decode Pub/Sub message
    message = base64.b64decode(event['data']).decode('utf-8')
    input_data = json.loads(message)

    # Initialize Vertex AI client
    aiplatform.init(project=PROJECT, location=REGION)

    endpoint = aiplatform.Endpoint(endpoint_name=ENDPOINT_ID)

    prediction = endpoint.predict([input_data])
    print("Prediction:", prediction.predictions)

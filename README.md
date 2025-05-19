🚗 Real-Time Fleet Monitoring and Predictive Maintenance System
Cloud-native, Real-time, AI-powered Vehicle Failure Prediction and Monitoring System
Built using Google Cloud Platform (GCP) services with Kubernetes orchestration.

📜 Project Description
This project simulates a real-world fleet monitoring system that predicts vehicle failures in real-time using synthetic sensor data, cloud ingestion pipelines, machine learning (Vertex AI), and Kubernetes-based orchestration.

The system enables:

Real-time vehicle telemetry ingestion

Failure prediction using a trained AutoML model

BigQuery storage for historical analysis

Live dashboards using Looker Studio

Kubernetes based automation for continuous data flow

🛠️ Technology Stack

Area	Tools Used
Data Ingestion	Cloud Pub/Sub
Data Processing	Cloud Functions
Prediction	Vertex AI AutoML Model
Data Storage	BigQuery
Visualization	Looker Studio
Orchestration	Google Kubernetes Engine (GKE)
Other	Docker, Python 3.10, Flask, Gunicorn

🗺️ Architecture Diagram


`🚀 Features
Real-time prediction of vehicle failures based on engine telemetry

Fully automated pipelines orchestrated via Kubernetes

Dynamic dashboarding of fleet health

Streaming synthetic telemetry data using a Kubernetes pod

Cloud-native serverless deployment using Cloud Functions

Optimized for cost awareness and real-time performance

📂 Project Structure

fleet-monitoring-system/
├── cloud-function/
│   ├── main.py
│   ├── requirements.txt
│
├── predictor-k8s/
│   ├── predictor_client.py
│   ├── Dockerfile
│   ├── predictor-deployment.yaml
│
├── architecture-diagrams/
│   ├── final-architecture.png
│   ├── kubernetes-orchestration.png
│
├── documentation/
│   ├── fleet-monitoring-project-report.pdf
│
├── README.md
└── LICENSE (optional)

🧠 How It Works
Data Simulation: Kubernetes deployment continuously generates synthetic telemetry data.

Cloud Function: Receives vehicle data via HTTP and triggers the Vertex AI endpoint.

ML Model: AutoML model predicts failure risk in real-time.

BigQuery Storage: Predicted results and raw telemetry are stored in BigQuery tables.

Dashboards: Looker Studio dashboards visualize fleet health live.

🔥 Future Improvements
Real-world telemetry integration

Auto-scaling predictor clients

Alert system for predicted failures (via SMS/Email)

Mobile-first monitoring app

Smart retraining based on data drift

Budget-optimized retraining policies

🧾 References
Google Cloud Pub/Sub Documentation

Google Cloud Dataflow Documentation

Google BigQuery Documentation

Vertex AI AutoML Documentation

Vertex AI Prediction Docs

Looker Studio Documentation

Google Cloud IAM Documentation

McKinsey Predictive Maintenance Report

📜 License
Distributed under the MIT License. See LICENSE for more information.
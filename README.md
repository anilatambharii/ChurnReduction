# ChurnReduction
Predictive Customer Churn Reduction for a Subscription-Based SaaS Business Problem Definition:

Python implementation using Flask for API deployment, scikit-learn for the ML model, and a simple dataset. This code trains a churn prediction model, exposes it via an API, and can be deployed to a cloud service like AWS or Heroku.

Requirements
Python 3.8+
Libraries: pandas, scikit-learn, flask, numpy
Install via: pip install pandas scikit-learn flask numpy

1. Deployment Instructions
    Local Testing:
    Save the code as churn_prediction.py.
    Run python churn_prediction.py.
    Test the API using curl or Postman:

curl -X POST -H "Content-Type: application/json" -d '{"usage_freq": 50, "payment_delay": 5, "support_tickets": 2}' http://localhost:5000/predict

2. Production Deployment (AWS EC2):
    Launch an EC2 instance (e.g., t2.micro, Ubuntu).
    SSH into the instance and install dependencies:

    sudo apt update
    sudo apt install python3-pip
    pip3 install pandas scikit-learn flask numpy

    Upload the model to the instance.
    Run the app in the background:

    nohup python3 churn_prediction.py &

    Open port 5000 in the EC2 security group.
    Access the API at http://<ec2-public-ip>:5000/predict

3. Scaling:
    Use a WSGI server like Gunicorn (pip install gunicorn) and run
    
    gunicorn --workers 4 --bind 0.0.0.0:5000 churn_prediction:app

    Add a load balancer (e.g., AWS ALB) for high traffic.

Production Notes
    Data: Replace the sample dataset with real customer data (e.g., CSV from your CRM).
    Monitoring: Add logging and metrics (e.g., Prometheus) to track model performance.
    Retraining: Schedule periodic retraining (e.g., monthly) using a cron job or CI/CD pipeline.
    Security: Add authentication (e.g., API keys) and HTTPS in production.


How to Test the App:

Since the app is running (as shown by Running on http://192.168.1.221:5000), you can interact with the defined endpoints:

Oprn a browser, type: curl http://192.168.1.221:5000/health ir use command line curl http://192.168.1.221:5000/health

curl -X POST -H "Content-Type: application/json" -d "{\"usage_freq\": 50, \"payment_delay\": 5, \"support_tickets\": 2}" http://192.168.1.221:5000/predict

Response: {"churn_prediction": 0, "churn_probability": 0.12}

Test connectivity: curl http://192.168.1.221:5000/health
use postman to test the API end point: {"usage_freq": 50, "payment_delay": 5, "support_tickets": 2}

Test in local machine : curl -X POST -H "Content-Type: application/json" -d "{\"usage_freq\": 50, \"payment_delay\": 5, \"support_tickets\": 2}" http://localhost:5000/predict




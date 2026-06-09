import psycopg2
import time
import boto3

cloudwatch = boto3.client("cloudwatch")

def report_failure():

    cloudwatch.put_metric_data(
        Namespace="DRSystem",
        MetricData=[
            {
                "MetricName": "DBHealth",
                "Value": 0,
                "Unit": "None"
            }
        ]
    )

def report_success():

    cloudwatch.put_metric_data(
        Namespace="DRSystem",
        MetricData=[
            {
                "MetricName": "DBHealth",
                "Value": 1,
                "Unit": "None"
            }
        ]
    )

while True:

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="demo",
            user="postgres",
            password="postgres"
        )

        conn.close()

        print("✅ DB Healthy")

        report_success()

    except Exception:

        print("❌ DB Failed")

        report_failure()

    time.sleep(10)

def lambda_handler(event, context):
    
    print("Hello from the Lambda function!")
    return {
        "statusCode": 200, 
        "body": "Hello from Lambda! Modified Again! Again!"
        }

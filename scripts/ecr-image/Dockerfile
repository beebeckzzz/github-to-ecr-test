FROM public.ecr.aws/lambda/python:3.10

# Copy function code
COPY app.py ./

# Install dependencies
RUN pip install python-dotenv

# Command to run the handler function
CMD ["app.lambda_handler"]
FROM python:3.9-slim

# Install dependencies
RUN pip install requests

# Copy your script into the Docker container
COPY slack_notify.py /slack_notify.py

# Set the entry point to your Python script
ENTRYPOINT ["python", "/slack_notify.py"]

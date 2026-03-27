# Use the official Python image
FROM python:3.11-slim

# Create a workspace inside the container
WORKDIR /app

# Copy ONLY the requirements first
COPY requirements.txt .

# Install the libraries (this happens inside the box)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app (main.py, .env)
COPY . .

# Open the port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
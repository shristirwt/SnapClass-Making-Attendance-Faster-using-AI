# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /code

# Install your heavy C++ system dependencies first
RUN apt-get update && apt-get install -y \
    cmake \
    libgl1 \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Hugging Face requires Docker spaces to run as a non-root user (UID 1000)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Copy your local project files into the cloud server
COPY --chown=user . /code

# Upgrade pip and install Python requirements
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Hugging Face requires apps to run on port 7860
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
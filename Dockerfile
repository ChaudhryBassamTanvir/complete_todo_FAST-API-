FROM python:3.11.5

# Update the package list and install system dependencies
RUN apt update && apt install -y \
    libpq-dev \
    python3-dev \
    pipx

# Ensure pipx is added to the PATH
RUN pipx ensurepath

# Install Poetry using pipx
RUN pipx install poetry

# Ensure Poetry's bin directory is in the PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory
WORKDIR /server

# Copy the project files
COPY . .

# Regenerate the lock file to ensure it matches the pyproject.toml
RUN poetry lock --no-update

# Install dependencies using Poetry
RUN poetry install

# Expose the application port
EXPOSE 8000

# Define the default command to run when the container starts
ENTRYPOINT [ "poetry", "run", "dev" ]

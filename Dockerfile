FROM python:3.10-slim

WORKDIR /app

# Install Poetry & project dependencies
COPY pyproject.toml poetry.lock* ./
RUN pip install --no-cache-dir poetry && poetry install --no-root

# Copy all source code
COPY . .

# Start FastAPI via Uvicorn
CMD ["poetry", "run", "uvicorn", "user_profile_service.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

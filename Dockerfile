FROM python:3.11-slim

RUN pip install --no-cache-dir flake8 pytest coverage line_profiler

WORKDIR /app

COPY . /app

CMD ["bash"]

FROM python:3.11

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "arena_backend.wsgi:application", "--bind", "0.0.0.0:8000"]

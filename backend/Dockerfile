FROM python:3.11-bullseye
WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip setuptools wheel pipenv
RUN pipenv install --deploy --ignore-pipfile
EXPOSE 8068
ENV PYTHONPATH=/app
CMD [ "pipenv", "run", "uvicorn", "--port", "8068", "--workers", "1", "--host", "0.0.0.0", "src.main:app" ]

FROM python:3.12.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYDEVD_DISABLE_FILE_VALIDATION 1

RUN mkdir /setup
COPY ./requirements.txt /setup
RUN pip install -r /setup/requirements.txt

RUN mkdir /app
COPY . /app/
RUN chmod +x /app/post.py

ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}

ENTRYPOINT ["python", "/app/post.py"]

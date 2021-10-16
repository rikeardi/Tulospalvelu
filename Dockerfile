FROM python:3.9

RUN apt-get update \
  && apt-get install -y \
    sqlite3 \
  && rm -fr /var/lib/apt/lists/* \
  && mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8001"]

FROM python:3.7.2-alpine

RUN apk update  && apk add postgresql-dev gcc python3-dev musl-dev 

RUN pip install psycopg2

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]


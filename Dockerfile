FROM python:3.5
COPY ./requirements.txt /

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD [ "python", "/tmp/example/app.py" ]


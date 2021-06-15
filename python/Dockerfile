FROM python:3.8

WORKDIR /usr/src/app
COPY main.py pip-requirements.txt .
RUN pip install -r ./pip-requirements.txt

CMD [ "python", "./main.py" ]

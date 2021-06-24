FROM python:3.8

WORKDIR /usr/src/app
COPY main.py requirements.txt ./
RUN pip install -r ./requirements.txt

CMD [ "python", "./main.py" ]

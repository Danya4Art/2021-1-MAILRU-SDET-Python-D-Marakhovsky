FROM python:3.8

ADD /requirements.txt requirements.txt
RUN pip3.8 install -r requirements.txt

COPY server.py /

CMD [ "python", "./server.py" ]
FROM python:3.6

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY client.py /app
CMD python client.py


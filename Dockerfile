FROM python:3.10

WORKDIR /home

COPY ./requirements.txt ./
RUN pip install -U pip && pip install -r requirements.txt
COPY . .

ENTRYPOINT ["python", "./main.py"]
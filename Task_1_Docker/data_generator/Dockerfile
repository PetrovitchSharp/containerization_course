FROM python:3.8

WORKDIR /datagen
COPY . .

RUN python -m venv env
RUN . ./env/bin/activate
RUN pip install -r requirements.txt

ENTRYPOINT python ./datagen.py


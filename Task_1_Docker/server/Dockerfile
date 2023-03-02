FROM python:3.8

WORKDIR /server
COPY . .

RUN python -m venv env
RUN . ./env/bin/activate
RUN pip install -r requirements.txt

ENTRYPOINT python ./app.py
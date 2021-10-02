FROM python:3.9.7-slim 
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -U -r /app/requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]

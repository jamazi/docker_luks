FROM python:slim-buster

WORKDIR /app
COPY . .
RUN apt update && \
    apt install --no-install-recommends -y cryptsetup && \
    pip install -r requirements.txt

CMD [ "python", "app.py" ]

EXPOSE 80
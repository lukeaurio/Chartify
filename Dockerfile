FROM python:3.9-alpine

WORKDIR /app

RUN pip3 install flask gunicorn spotipy pip-system-certs plotly lyricsgenius

COPY . .

CMD [ "gunicorn", "-w 4", "-b", "0.0.0.0:5000", "app:app", "--access-logfile=-"]
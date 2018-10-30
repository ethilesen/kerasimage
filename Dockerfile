FROM ubuntu:18.04
COPY requirements.txt /
RUN apt update && \
    apt install -y python3 python3-pip && \
    pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python3", "manage.py", "start", "0.0.0.0:5000"]

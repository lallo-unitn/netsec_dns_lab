FROM "kathara/base"

RUN apt-get update -y && apt install -y python3 python3-venv scapy dnsutils iputils-ping python3-pip
RUN pip install flask requests
RUN echo python3 -m flask --version

FROM "ubuntu:22.04"

RUN apt-get update -y && apt-get install -y wget && apt-get install xz-utils && apt-get install -y libuv1
RUN apt-get install -y build-essential
RUN wget -r -P /tmp/9.15.8/ ftp://ftp.isc.org/isc/bind9/9.15.8
RUN mkdir /tmp/install
WORKDIR /tmp/9.15.8/ftp.isc.org/isc/bind9/9.15.8
RUN tar -xvf bind-9.15.8.tar.xz
WORKDIR /tmp/9.15.8/ftp.isc.org/isc/bind9/9.15.8/bind-9.15.8/
RUN ./configure
RUN make

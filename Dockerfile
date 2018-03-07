FROM resin/rpi-raspbian:jessie
MAINTAINER Brandon Gulla <im@brandongulla.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-setuptools \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*


RUN easy_install Flask
RUN easy_install mimerender
RUN easy_install flask-cors
EXPOSE 8080

ADD ./bin/ds18b20.py /
ADD ./bin/app.py /
RUN chmod +x /app.py

CMD ["/app.py"]





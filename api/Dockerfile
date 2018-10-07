FROM ubuntu:16.04

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    nginx \
    libpcre3 libpcre3-dev \
    supervisor && \
    pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

# Install uwsgi (here because it takes a while)
RUN pip3 install uwsgi

# Setup all the config files
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY ./conf/nginx-app.conf /etc/nginx/sites-available/default
COPY ./conf/supervisor-app.conf /etc/supervisor/conf.d/

# Install project requirements
COPY ./requirements.txt ./
RUN pip3 install -r ./requirements.txt

# Install our code
ENV API_PATH /usr/src/api
ADD . ${API_PATH}/

EXPOSE 5000

# Entrypoint script, that will build js bundle before running the server
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/supervisord", "--configuration=/etc/supervisor/conf.d/supervisor-app.conf"]

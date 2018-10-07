FROM ubuntu:16.04
# General
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git \
    curl \
    nginx \
    libpcre3 libpcre3-dev
    # nodejs
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs
# Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install yarn

# ADD ./package.json ./yarn.lock ./
# Adding app files
ENV APP_PATH /usr/src/app
RUN mkdir -p ${APP_PATH}
WORKDIR ${APP_PATH}
COPY package.json yarn.lock ./
RUN yarn install
COPY . ./
WORKDIR /

# Nginx config - modify copy custom conf file to /etc/nginx/sites-enabled/default here if needed
EXPOSE 80

# Entrypoint script, that will build js bundle before running the server
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

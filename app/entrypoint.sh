#!/bin/bash
set -e

# If app directory exists, which happens at image build
if [ -d $APP_PATH ]; then
    # Building javascript bundle
    echo "[INFO] Building js bundle..."
    cd $APP_PATH
    yarn build
    cd
    # Publishing bundle and removing source code
    cp $APP_PATH/build/* /var/www/html/
    rm -rf $APP_PATH
    # At image build, docker CMD runs nginx
    echo "[INFO] Running nginx..."
fi

exec "$@"

FROM node:18-alpine3.15
ARG TZ=Asia/Tokyo
ARG WWWUSER_PUID=2345
ARG WWWUSER_PGID=2345

LABEL maintainer="yuruto"
LABEL description="build django-rest-framework"

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    SRC_ROOT_PATH=/code \
    APP_PORT=3000 \
    PUID=1000 \
    PGID=1000

COPY ./requirements.txt /requirements.txt

# Install
RUN    apk --no-cache update \
    && apk add --no-cache bash tzdata gettext pcre-dev mysql-client bind-tools libuuid su-exec \
                         mariadb-dev mariadb-connector-c-dev libsodium libxml2-dev tini shadow \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    \
    # Install temporary libraries
    \
    && apk add --no-cache --virtual .build-deps \
               gcc musl-dev libffi-dev g++ libgcc libstdc++ libxslt-dev python3-dev \
               libc-dev linux-headers openssl-dev curl \
    && apk add --no-cache python3 \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools \
    \
    # Create symbolic link
    \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && ln -sf /usr/bin/pip3 /usr/bin/pip \
    \
    # Install python libraries
    \
    && pip install -r /requirements.txt \
    \
    # Delete temporary libraries
    \
    && apk --purge del .build-deps \
    && mkdir -p ${SRC_ROOT_PATH} \
    && mkdir /data \
    && rm -rf /root/.cache /var/cache/apk/* /tmp/*

# change working directory
WORKDIR ${SRC_ROOT_PATH}
# add shell script
COPY ./execute.sh /usr/local/bin/execute.sh
RUN chmod 755 /usr/local/bin/execute.sh

ENTRYPOINT ["/sbin/tini", "-e", "143", "--"]
CMD ["/usr/local/bin/execute.sh"]
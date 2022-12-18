FROM node:18-alpine3.15
ARG TZ=Asia/Tokyo

LABEL maintainer="yuruto"
LABEL description="build react"

ENV PUID=1000 \
    PGID=1000

RUN    apk --no-cache update \
    && apk add --no-cache bash tzdata shadow su-exec tini \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && rm -rf /home/node/app \
    && rm -rf /root/.cache /var/cache/apk/* /tmp/*

COPY ./execute.sh /usr/local/bin/execute.sh
RUN chmod 755 /usr/local/bin/execute.sh

USER node
RUN    cd /home/node \
    && echo -e "y\n" | npx create-react-app app -timeout=60000 \
    && cd app \
    && npm install axios jwt-decode @react-oauth/google@latest
USER root

WORKDIR /home/node/app

ENTRYPOINT ["/sbin/tini", "-e", "143", "--"]
CMD ["/usr/local/bin/execute.sh"]
#!/bin/bash

# change uid and gid
_uid=$(id -u node)
_gid=$(id -g node)

# change GID
if [ -n "${PGID}" ] && [ ${PGID} -ne ${_gid} ]; then
    groupmod -g ${PGID} node
fi
# change UID
if [ -n "${PUID}" ] && [ ${PUID} -ne ${_uid} ]; then
    usermod -u ${PUID} node
fi

# update owner
chown node:node package.json package-lock.json
# execute process by node user
su-exec node:node npm start
#!/bin/bash

# change uid and gid
_uid=$(id -u node)
_gid=$(id -g node)

if [ -n "${PUID}" ]; then
    _uid=${PUID}
fi
if [ -n "${PGID}" ]; then
    _gid=${PGID}
fi

readonly tmpgid=34512
groupadd -g ${tmpgid} tmpgroup
usermod -g tmpgroup node
groupdel node
groupadd -g ${_gid} node
usermod -g ${_gid} node
usermod -u ${_uid} node
groupdel tmpgroup

if [ "${DJANGO_APP_ENV}" = "development" ]; then
    su-exec node:node python manage.py makemigrations
    su-exec node:node python manage.py migrate
    su-exec node:node python manage.py runserver 0.0.0.0:${BACKEND_PORT}
else
    # Waiting for MySQL database to be ready...
    db_cmd="mysql -h ${DB_HOST} -u ${MYSQL_USER} -p${MYSQL_PASSWORD} -P ${DB_PORT}"
    counter=1

    while ! ${db_cmd} -e "show databases;" > /dev/null 2>&1; do
        sleep 1
        counter=$(expr ${counter} + 1)
    done
    echo "[Django]" $(date "+%Y/%m/%d %H:%M:%S") MySQL database ready! "(${counter}sec)"

    # Create ini file
    readonly env_vars=$({
        echo '$$BACKEND_PORT'
        echo '$$SRC_ROOT_PATH'
    } | tr '\n' ' ')
    cat /data/uwsgi.template | envsubst "${env_vars}" > /data/uwsgi.ini

    su-exec node:node python manage.py makemigrations
    su-exec node:node python manage.py migrate
    # Execute uWSGI
    uwsgi --ini /data/uwsgi.ini
fi
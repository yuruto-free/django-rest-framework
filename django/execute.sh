#!/bin/bash

# change uid and gid
_uid=$(id node)
_gid=$(id node)

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
    python manage.py runserver ${APP_PORT}
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
        echo '$$APP_PORT'
        echo '$$SRC_ROOT_PATH'
    } | tr '\n' ' ')
    cat /data/uwsgi.template | envsubst "${env_vars}" > /data/uwsgi.ini

    # Execute uWSGI
    uwsgi --ini /data/uwsgi.ini
fi
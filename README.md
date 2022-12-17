# Django REST framework
## Preparation
1. Create `.env` file in `./envs/django` with reference to [the README.md](./envs/django/README.md).
1. Create `.env` file in `./envs/mysql` with reference to [the README.md](./envs/mysql/README.md).
1. Check `.env` files exist.

    ```bash
    ls envs/*/.* | grep "\.env$"
    # results:
    #   envs/django/.env
    #   envs/mysql/.env
    ```

1. Update `PUID` and `PGID` in `docker-compose.yml`. These IDs can be obtained by executing the following command.

    ```bash
    id ${USER}
    # output example
    # uid=1000(yuruto) gid=1000(yuruto) groups=1000(yuruto)
    # PUID = 1000 (= uid), PGID = 1000 (= gid)
    ```

## Build
Run the following command.

```bash
docker-compose build --no-cache
docker images | grep none | awk '{print $3;}' | xargs -I{} docker rmi {}
```

## Start
1. Migrate the database with reference to [the README.md](./django/README.md).
1. Enter the following command to start the container.

    ```bash
    docker-compose up -d
    ```

## Check log/status
Execute the following command.

```bash
# show process status
docker-compose ps

# show log
docker-compose logs
```
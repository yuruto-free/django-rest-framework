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

1. Setup Django with reference to [the README.md](./django/README.md).

## Build
Run the following command.

```bash
./wrapper.sh build
```

## Start containers
Enter the following command to start the containers.

```bash
./wrapper.sh start
```

## Stop containers
Execute the following command to stop containers.

```bash
./wrapper.sh stop
```

## Restart containers
Enter the following command to restart the containers.

```bash
./wrapper.sh restart
```

## Delete containers
Run the following command to delete containers.

```bash
./wrapper.sh down
```

## Check log/status of containers
Execute the following command.

```bash
# show process status
./wrapper.sh ps

# show log
./wrapper.sh logs
```
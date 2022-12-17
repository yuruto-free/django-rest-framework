# Define environment variables
## `.env` file
Create an environment variable configuration file `.env` in the following format.

```bash
MYSQL_ROOT_PASSWORD=djangorootpassword
MYSQL_DATABASE=django
MYSQL_USER=djangouser
MYSQL_PASSWORD=djangopassword
```

A function of each environment variable is given below.

| Env   | Function |
| :---- | :----    |
| MYSQL_ROOT_PASSWORD | MySQL root password |
| MYSQL_DATABASE      | Database name |
| MYSQL_USER          | Username of database |
| MYSQL_PASSWORD      | Password of `MYSQL_USER` |

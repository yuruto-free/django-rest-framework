# Define environment variables
## `.env` file
Create an environment variable configuration file `.env` in the following format.

```bash
DJANGO_APP_ENV=development
DJANGO_SECRET_KEY=abcdefghijklmnopqrstuvwxyz0123456789
DJANGO_WWW_VHOST=www.example.com,sub.example2.com
DJANGO_SUPERUSER_NAME=superuser
DJANGO_SUPERUSER_PASSWORD=superuserpassword
```

A function of each environment variable is given below.

| Env   | Function |
| :---- | :----    |
| DJANGO_APP_ENV | Application environment. Set development or production. |
| DJANGO_SECRET_KEY | Django secret key. Set arbitrary value. |
| DJANGO_WWW_VHOST | Allowed hosts of Django. |
| DJANGO_SUPERUSER_NAME | Username of superuser. Set 128 characters allowing only Unicode characters, in addition to @, ., +, -, and _. |
| DJANGO_SUPERUSER_PASSWORD | Password of superuser. Set 128 characters allowing only Unicode characters, in addition to @, ., +, -, and _. |
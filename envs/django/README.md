# Define environment variables
## `.env` file
Create an environment variable configuration file `.env` in the following format.

```bash
DJANGO_APP_ENV=development
DJANGO_SECRET_KEY=abcdefghijklmnopqrstuvwxyz0123456789
DJANGO_WWW_VHOST=www.example.com,sub.example2.com
DJANGO_SUPERUSER_USERNAME=superuser
DJANGO_SUPERUSER_EMAIL=superuser@project.com
DJANGO_SUPERUSER_PASSWORD=superuserpassword
DJANGO_SOCIAL_GOOGLE_OAUTH2_KEY=google-oauth2-key
DJANGO_SOCIAL_GOOGLE_OAUTH2_SECRET=google-oauth2-secret
```

A function of each environment variable is given below.

| Env   | Function |
| :---- | :----    |
| DJANGO_APP_ENV | Application environment. Set development or production. |
| DJANGO_SECRET_KEY | Django secret key. Set arbitrary value. |
| DJANGO_WWW_VHOST | Allowed hosts of Django. |
| DJANGO_SUPERUSER_USERNAME | Username of superuser. Set 128 characters allowing only Unicode characters, in addition to @, ., +, -, and _. |
| DJANGO_SUPERUSER_EMAIL | Email of superuser. Set 128 characters allowing only Unicode characters, in addition to @, ., +, -, and _. |
| DJANGO_SUPERUSER_PASSWORD | Password of superuser. Set 128 characters allowing only Unicode characters, in addition to @, ., +, -, and _. |
| DJANGO_SOCIAL_GOOGLE_OAUTH2_KEY | Google OAuth client key. |
| DJANGO_SOCIAL_GOOGLE_OAUTH2_SECRET | Google OAuth client secret key. |

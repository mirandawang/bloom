# secret settings
# copy to secret.py

# used for django's cryptographic signing, 50 characters long
# you can generate one here http://www.miniwebtool.com/django-secret-key-generator/

SECRET_KEY = 'bloomel8*t3$fe%mt4lbqp*t_211nhcclo--)zs$-l8+m3*uk-i1$1w'

# These configurations are partially set by default for a local development environment. Remember to use a strong passphrase for deployment. Use the username and password you configured creating the database while following the README. Change the database name, host, or port as necessary for deployment.

DB_NAME = 'bloom'
DB_USER = 'django'
DB_PASSWORD = 'test'
DB_HOST = 'localhost'
# often left blank
DB_PORT = ''

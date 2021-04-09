# First Django Website

This website is created for educational purposes.
It stores and allocates some tasks to freelancers who are registered in the website.

## Building the source code

### Installing dependencies

First, you need to install *postgresql* on your machine.
To install it on Ubuntu open a terminal and run the following command:

```bash
 sudo apt-get install postgres
```

Next, make sure *pip* is installed on your machine or install it by running
the following lines:

```bash
 sudo apt-get install python3
 sudo apt-get install python3 - pip
```

After installing *pip*, install *virtualenv* on your machine:

```bash
 sudo pip3 install virtualenv
```

Now, initiate a virtual environment by running the following command in
your project's root directory:

```bash
 virtualenv .venv
```

Activate it by running this command:

```bash
 source .venv/bin/activate
```

Finally, install all requirements:

```bash
 sudo pip3 install -r requirements.txt
```

### Configuring the database

Now you must switch user to *postgres* and change your password:

```bash
 sudo su - postgres
 psql
```

```sql
# \password
```

And, enter a new password.

Now, you need to change the database password in *myfirstws/settings.py*:
Open the file *myfirstws/settings.py* with a text editor, scroll down
to **DATABASES** and change the username and password fields to your postgres
username and password.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'website_db',
        'USER': 'ENTER YOUR USERNAME HERE',
        'PASSWORD': 'ENTER YOUR PASSWORD HERE',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

```

### Migrating the models

Migrate models to the database by running this command

```bash
 sudo python3 manage.py migrate
```

### Deploying the website (development)

Run this command to deploy the app on port 8000:

```bash
 sudo python3 manage.py runserver
```


# First Django Website

This website is created for educational purposes. It stores and allocates some tasks to freelancers who are registered in the website. 

## Building the source code

First of all, you need to install *postgresql* on your machine.
To install it on Ubuntu open a terminal and run the following command:

`$ sudo apt-get install postgres`

Now you must switch user to *postgres* and change your password:

`$ sudo su - postgres`
`$ psql` 
`# \password` 
 
And, enter new password.


Next, make sure *pip* is installed on your machine or install it by running the following lines:

`$ sudo apt-get install python3`
`$ sudo apt-get install python3-pip`

After installing *pip* install *virtualenv* on your machine:

`$ sudo pip3 install virtualenv`

Now, initiate a virtual environemnt by running the following command in your project's root directory:

`$ virtualenv .venv`

Activate it by running this command:

`$ source .venv/bin/activate`

Finally, install all requirements:

`$ sudo pip3 install -r requirements.txt`

Now, open the the file *myfirstws/settings.py* with a text editor, scroll down to **DATABASES**  and change the username and password field to your postgres username and password. 

Migrate models to the database by running this command;

`$ sudo python3 manage.py migrate`

Run this command to deploy the app on port 8000:

`$ sudo python3 manage.py runserver`



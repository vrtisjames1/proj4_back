
# Username: admin
# Password: admin

## START UP
new directory tab: 
source ~/ga-env/bin/activate

python -m pip install Django

## must be in directory for this command: 
(AFTER FIRST TIME CAN START OFF WITH THIS & source ~/ga-env/bin/activate)
django-admin startproject proj4_back

cd django_rest_api
python manage.py startapp connect4

## WITHIN PSQL
psql
CREATE DATABASE proj4_back;
(verify with \l)

## next:
change subfolder to follwing:
FOLDER: settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_api',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

(IF DOESNT WORK THEN CAHNGE LOCAL HOST TO 12701.1??)

## NEXT
python -m pip install psycopg2-binary

### COMMAND TO SETUP TABLES IN DATABASE. TERMINAL COMMANDS TO RUN SQL for us
python manage.py migrate
(verify with \dt in psql)

### change installed apps in SETTINGS.PY
### include app name that was created (i.e. contacts_api)
INSTALLED_APPS = [
    'connect4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


## Next: models folder in api

class Contact(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

## Next setup migration and execute
python manage.py makemigrations connect4
python manage.py sqlmigrate connect4 0001

### look at psql table afterwards to see updated tables
python manage.py migrate

python manage.py shell

## Once it's started, we can write python to play around with the models. In the shell runt he following to add data:

from connect4.models import Connect4
Connect4.objects.all() # get all the contacts in the db
c = Contact(name="Matt", age=40) # create a new contact.  Note this isn't yet in the db
c.save() # save the contact to the db
c.id # check the id to make sure it's in the db
Contact.objects.all()
Contact.objects.all()[0]
Contact.objects.all()[0].name
Contact.objects.all()[0].age
quit()

## next
python manage.py createsuperuser
#### create username
#### create password

## Now add the following to contacts_api/admin.py

from .models import Contact
admin.site.register(Contact)

## and in the terminal run

python manage.py runserver

## now that the server is running in your browser check if the server is running
http://localhost:8000/

http://localhost:8000/admin
### input username and password, now you can see your data

# Create api endpoints
## Install djangorestframework:

python -m pip install djangorestframework

### back into settings.py
INSTALLED_APPS = [
    'rest_framework',  # add this
    'contacts_api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

## Create contacts_api/serializers.py and add in file

### serializers.py

from rest_framework import serializers 
from .models import Contact 

class ContactSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Contact # tell django which model to use
        fields = ('id', 'name', 'age',) 
### tell django which fields to include


## Next: set contacts_api/views.py to

from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ContactSerializer # tell django what serializer to use

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer


## set contact/urls.py edit

from django.urls import path
from . import views

urlpatterns = [
    path('api/contacts', views.ContactList.as_view(), name='contact_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/contacts/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'), # api/contacts will be routed to the ContactDetail view for handling
]

## set django_rest_api/urls.py edit
from django.contrib import admin
from django.urls import path
from django.conf.urls import include # add this

urlpatterns = [
    path('', include('contacts_api.urls')), # add this
    path('admin/', admin.site.urls),
]

## Now you can use your URLS in DJANGO (i.e. localhost:8000/api/cotantats)

## Next: add CORS
python -m pip install django-cors-headers

## edit django_rest_api/settings.py to include the new package:

INSTALLED_APPS = [
    'corsheaders', # add this
    'rest_framework',
    'contacts_api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # this makes the cors package run for all requests.  A bit like app.use() in express
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True # add this

## POSTMAN
GET LINK
HEADERS>>
ORIGIN

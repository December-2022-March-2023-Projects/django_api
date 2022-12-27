API
=

An API(Application Programming Interface) is a software that allow two applications to talk to each other.

DJANGO REST FRAMEWORK
-


- A RESTful API is an API that uses HTTP requests to GET, PUT, POST and DELETE 

- REpresentational State Transfer

- REST is prefered over SOAP(Simple object access protocol ) due to the less REST leverages less bandwidth.

- REST is an architectural style for developing web services.

DRF is a powerfil and flexible toolkit for building web APIS:

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down – just use regular function-based views if you don’t need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.

Types of API Requests
-

- HTTP GET:Used to retrieve resource representation ie getting data.
- HTTP POST: Used to create new resources ie Posting data
- HTTP PUT: Used to update existing resources ie Editing data
- HTTP DELETE: Used to delete resources ie Deleting data

Why would you need an API
-

- Make money selling data.
- Developing a mobile app.
- Let other developers integrate your content on their site.

Django REST Framework
-

- A powerful web toolkit for building web APIs .
- Suitable for building web APIs for Django applications
- Requirements:
  - A django application
  - Python -v (3.5, ...)
  - Django -v (1.11, ...)

- Installation

  ```
  pip3 install djangorestframework
  ```

[Serialization](https://www.django-rest-framework.org/api-guide/serializers/)
-

- `Serializers` Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

- The serializers in REST framework work very similarly to Django's Form and ModelForm classes. We provide a Serializer class which gives you a powerful, generic way to control the output of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.

Migrations
-

```
python manage.py makemigrations <app_name>
python manage.py sqlmigrate <app_name> <migration number>
python manage.py migrate
```

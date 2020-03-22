# Django RealEstate Web Application Project

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject projectname

$ cd projectname/
$ Edit settings.py
$ python manage.py migrate
$ python manage.py runserver
```

## Demo
[https://sceptre01-realestate.herokuapp.com](https://sceptre01-realestate.herokuapp.com)

[https://sceptre01-realestate.herokuapp.com/admin](https://sceptre01-realestate.herokuapp.com/admin)
(admin:admin)

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Property Listings, Agent Listings, User Login/Register, Admin Area, Inquiries
* Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.

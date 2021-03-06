# Amcom Challenge 
Challenge for hiring at Amcom company.
The project is point of Sale system.

[![Build Status](https://travis-ci.org/anderson89marques/wttdv3.svg?branch=master)](https://travis-ci.org/anderson89marques/point_of_sale)
[![codecov](https://codecov.io/gh/anderson89marques/point_of_sale/branch/master/graph/badge.svg)](https://codecov.io/gh/anderson89marques/point_of_sale)

# Tools and main libraries used for this challenge

```
Linux, Notebook Dell i5, VSCode(IDE), python 3.8.0, django, 
django-rest-framework, pylint, isort, autopep8, python-decouple
postgres, reactjs, docker, docker-compose
```

## How Run the project using docker
You need docker and docker-compose installed. (They need run without sudo)
I use the latests versions of them.  

- Clone repository
```console
git clone https://github.com/anderson89marques/point_of_sale
```

- Change directory into your newly created project.
```console
cd point_of_sale
```

- Run docker compose
```console
docker-compose up --build
```

A initial data was created.
You can use `postman` collections that are in `backend/postman` folder to access the backend API.
You can see the api doc acessing `/swagger` path 


## Model Diagram

![Alt text](doc_images/diagrama.png?raw=true "Home")

## How Test and Run the project backend locally (without docker)

 Clone repository
```console
git clone https://github.com/anderson89marques/point_of_sale
```

- Change directory into your newly created project.
```console
cd point_of_sale
```

- Create a Python virtual environment. (I use pyenv, so here 'python' is a link for python 3.8.0)
```console
python -m venv .venv
```

- Activate virtual environment.
```console
source .venv/bin/activate
```

- Install dependencies and make migrations. 
```console
make local_start
```

- Run project's tests.
```console
make test
```

- Run project backend
```console
make runserver
```

## How Test and Run the project frontend locally (without docker)

You need node instaled and npm or yarn. (Below steps use yarn).
You need run backend again or frontend don't work in right way.

Clone repository
```console
git clone https://github.com/anderson89marques/point_of_sale
```

- Change directory into your newly created project.
```console
cd point_of_sale/frontend
```

- Install dependencies using yarn. 
```console
yarn 
```

- Run frontend project at dev environment.
```console
yarn start
```

- Run Tests
```console
yarn test
```

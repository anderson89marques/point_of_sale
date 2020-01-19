# AMcom Challenge 
Challenge for hiring at Luizalabs company.
The project is point of Sale system.

# Tools and main libraries used for this challenge

```
Linux, Notebook Dell i5, VSCode(IDE), python 3.8.0, django, 
django-rest-framework, pylint, isort, autopep8, python-decouple
postgres, reactjs
```

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
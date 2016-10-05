# flaskApp

Building a basic web application with Flask/Python.

## Getting Started

```
git clone https://github.com/scottfabini/flaskApp.git
```

### Prerequisities

[Python](https://www.python.org/downloads/)installed on your system.
VirtualEnv

### Installing

```
git clone https://github.com/scottfabini/flaskApp.git
cd flaskApp
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py shell
>>> db.create_all()
python manage.py db upgrade
python manage.py runserver
Open a web browser and navigate to 127.0.0.1:5000
```

## Contributing

Contributions are not being accepted at this time.

## Authors

* **Scott Fabini** - *Initial work* - [Scott](https://github.com/scottfabini)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Based on the book "Flask Web Development" by Miguel Grinberg

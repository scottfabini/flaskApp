# flaskApp

Building a basic web application with Flask/Python. When users enter their names, it is stored in a database.  These names persist across sessions.

![Image of flaskApp1](https://raw.githubusercontent.com/scottfabini/flaskApp/master/app/static/FlaskApp1.png)

![Image of flaskApp2](https://raw.githubusercontent.com/scottfabini/flaskApp/master/app/static/FlaskApp2.png)

## Getting Started

```
git clone https://github.com/scottfabini/flaskApp.git
```

### Prerequisities

[Python](https://www.python.org/downloads/) and 
[VirtualEnv](https://virtualenv.pypa.io/en/stable/) installed on your system.

### Installing

```
virtualenv venv
source venv/bin/activate
git clone https://github.com/scottfabini/flaskApp.git
cd flaskApp
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

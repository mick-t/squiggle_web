# squiggle_web
Web implementation of the Squiggle DNA Sequence Visualization

Still under development.

Steps to run:

* Create a Python 3.6+ virtualenv.
* Source the virtualenv.
* Install the required dependencies:

 `pip install -r requirements.txt`
* Run the app:

`python manage.py runserver`

**Note**: use the dev setting file, production isn't ready yet.

Using the development version (using django debug tool, & Werkzeug):
* Install the additional required dependencies:

`pip install -r requirements-debug.txt`
* Run the app:

`python manage.py runserver  --settings=squiggle_web.dev

See the sample view at:

<http://127.0.0.1:8000/squiggle_views/>
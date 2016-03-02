# General description
AskItTask is an open-source task-management tool built with Django, AngularJS and good intentions.

##  To try out:
Run ```python3 -m "http.server"``` or ```python2 -m "SimpleHTTPServer"``` and visit localhost:8000. 

## Development setup
Run ```bower install``` and  ```gulp``` in command line to download and compile all front end dependencies.

## Testing
To run test suite make sure you have Python 2.7, Chrome webbrowser and chromedriver installed and run following commands:

```
pip install -r python_deps/linux_test_requirements.txt
python2 -m "py.test" tests/tests.py
```

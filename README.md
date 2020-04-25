# Web IR
Web IR is a web server that exposes a REST-like API in order to send commands to a local LIRC daemon.

## Run locally
In order to start the web server on a development environment, run the `run.py` file:<br>
`python run.py`

## Package
This project is setup with `setuptools` for packaging.
Make sure you have `wheel` installed and then use the `setup.py` script to package the project:<br>
`python setup.py sdist bdist_wheel`
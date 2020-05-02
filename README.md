# Web IR
Web IR is a web server that exposes a REST-like API in order to send commands to a local LIRC daemon.

## Run locally
In order to start the web server on a development environment, run the `run.py` file:<br>
`python run.py`

## Configuration
The application packages a [configuration by default](./webir/config.py).
This configuration should be enough for development and production.
However, when deploying to production, the configuration can be overridden with a production configuration:
* Create a configuration file in production, for example `/path/to/config.py`
* Then export the configuration in the `WEBIR_CONFIGURATION` environment variable: `export WEBIR_CONFIGURATION=/path/to/config.py`
* Run the application and the environment variable configuration will override the default distributed configuration.

## Package
This project is setup with `setuptools` for packaging.
Make sure you have `wheel` installed in your virtual environment and then use the `setup.py` script to package the project:
```shell script
python setup.py sdist bdist_wheel
```
**Note:** The application should be packaged within the virtual environment.

## Vagrant
A Vagrant environment is set up in order to test the deployment with the production WSGI HTTP Server `gunicorn`.
`Gunicorn` is not compatible with Windows, so in order to test the deployment of the application on this production-ready server we need a Unix VM.
The VM is already provisioned with the WebIR application and a Gunicorn server.
To run the application on Gunicorn in the VM, follow these instructions:
* Activate the Python virtual environment:
```shell script
source venv/bin/activate
```
* Run the application on Gunicorn with the default configuration:
```shell script
gunicorn -b 0.0.0.0:8080 "webir:create_app()"
```
* Reinstall after modifications: After having modified the sources and repackaged the application, the package can be reinstalled:
````shell script
pip install dist/webir-0.1.0-py3-none-any.whl --force-reinstall
````
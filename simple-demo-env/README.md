Use the Agent's embedded python to run the simple flask application. (Note: you can use your system's Python environment as long as it is >= 3.7 and have Flask installed)

Embedded python location:

* Windows: `C:\Program Files\Datadog\Datadog Agent\embedded3\python.exe`
* Mac/Linux: `/opt/datadog-agent/embedded/bin/python3.7`

Install flask to the embedded Python environment.

* Windows: `& 'C:\Program Files\Datadog\Datadog Agent\embedded3\python.exe' -m pip install flask`
* Mac/Linux: `/opt/datadog-agent/embedded/bin/python3.7 -m pip install flask`

Run the application:

* Windows: `& 'C:\Program Files\Datadog\Datadog Agent\embedded3\python.exe' \path\to\flask_app.py`
* Mac/Linux: `/opt/datadog-agent/embedded/bin/python3.7 /path/to/flask_app.py`

Use your browser and `curl`/`IWR` to hit the endpoints multiple times:

* Windows: `IWR https://localhost:5050/`
* Windows: `curl https://localhost:5050/`

Note: if port `5050` is already being used on your host, change the port the flask app uses on [line 33](https://github.com/dixonscottr/dd-partner-app/blob/master/simple-demo-env/flask_app.py#L33)

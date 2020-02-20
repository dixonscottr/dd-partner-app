# Script to submit a few logs

Both scripts submit example logs in the following format:

```
[Fri, 29 Mar 2019 12:00:57 -0700] Some text here that isn't JSON. [Message Begins] {"key": "value", "another_key": "another_value", "measure_one": 9, "status": "INFO", "url": "https://testsite.com/geocyclic?page=38#axillar"} [user2]
```

## Notes for `submit-logs.py`

- Requires python > 3.3
- On windows, use the agent's embedded python located at `C:\Program Files\Datadog\Datadog Agent\embedded3\python.exe` and run the following:
```
$ENV:DD_API_KEY="API_KEY"
& 'C:\Program Files\Datadog\Datadog Agent\embedded3\python.exe' path\to\submit_logs.py
```

- On linux or mac, run the script with:
```
/opt/datadog-agent/embedded/bin/python3 submit_logs.py
```


## Notes for `submit-logs.sh`

- On Mac make sure that `shuf` is installed or run `brew install coreutils`
- Make sure the script is executable or run:

```
sudo chmod -x submit-logs.sh
```

Run the script with: 

Mac/Linux
```
export DD_API_KEY=<KEY> & sh submit-logs.sh $DD_API_KEY
```

note: You may need to install the `wamerican` package on Linux

```
apt-get install --reinstall wamerican
```

## Grok Parser

Use the following parsing rule to set up the Grok parser

```
parser_rule_1 \[%{date("EEE, dd MMM yyyy HH:mm:ss Z"):log_date}\] %{data:log_message} \[Message Begins\] %{data::json} \[%{word:username}\]

```


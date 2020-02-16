import time
import random
from flask import Flask, request
from ddtrace import config, tracer, patch_all

patch_all()

config.analytics_enabled = True

app = Flask(__name__)

@tracer.wrap()
def make_another_span():
	time.sleep(random.random())

@app.route('/')
def index():
    ## uncomment below to add custom metadata https://docs.datadoghq.com/tracing/guide/add_span_md_and_graph_it/?tab=python#instrument-your-code-with-custom-span-tags
    # current_span = tracer.current_span()
    # user_agent = request.headers.get('User-Agent')
    # if current_span and user_agent:
    #     current_span.set_tag('user_agent', user_agent)
    return 'hello world'

@app.route('/error')
def error():
    ## uncomment below to add additional span
    # make_another_span()
    # intentional IndexError 
    return 'error'[90]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
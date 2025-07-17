import os

workers = int(os.environ.get('WEB_CONCURRENCY', 4))
threads = int(os.environ.get('PYTHON_THREADS', 1))
bind = "0.0.0.0:" + os.environ.get('PORT', '5000')
worker_class = 'sync'
loglevel = 'info'
accesslog = '-'
errorlog = '-'
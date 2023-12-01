from multiprocessing import cpu_count
from os import environ

def max_workers():
    return cpu_count()


bind = '0.0.0.0:' + environ.get('PORT', '8080')
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()

env = {
    'DJANGO_SETTINGS_MODULE': 'ghost_fnk.settings'
}

reload = True
name = 'Project_name'
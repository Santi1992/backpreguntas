import multiprocessing
import os

timeout=30
bind = '172.31.85.47:8080'
worker_class = 'gthread'
max_requests = 3
#worker_tmp_dir = "/dev/shm"  Si lo corrremos con docker
workers = (multiprocessing.cpu_count()*2)+1
threads = 2
#FLASK_DEBUG=True
#PROPAGATE_EXCEPTIONS=True config de flask.
#certfile = 'itshopseghomo.redlink.com.ar.cer'
#keyfile = 'itshopseghomo.redlink.com.ar.key'

# INVERTIR EN PRODUCCIÓN
debug =False
reload=True
# PARA CORRER
#gunicorn -c 'confgunicorn.py' 'configApp:create_app(env="local")'
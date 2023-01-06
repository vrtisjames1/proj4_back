web: gunicorn proj4_back.wsgi
release: python manage.py migrate
web2: daphne proj4_back.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2
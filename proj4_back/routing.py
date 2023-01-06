import os
import proj4_back.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj4_back.settings")
channel_layer = proj4_back.asgi.get_channel_layer()
import os

WINDOW_WIDTH = os.environ.get('WINDOW_WIDTH', 600)
WINDOW_HEIGHT = os.environ.get('WINDOW_HEIGHT', 800)
WINDOW_CAPTION = os.environ.get('WINDOW_CAPTION', 'Something...')

TIME_DELAY = os.environ.get('TIME_DELAY', 100)
DEBUG_MODE = os.environ.get('DEBUG_MODE', True)
DEBUG_POSITION = os.environ.get('DEBUG_POSITION', (600, 10))

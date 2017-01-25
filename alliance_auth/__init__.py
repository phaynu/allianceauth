from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celeryapp import app as celery_app  # noqa

import subprocess
try:
    __version__ = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8').split('\n')[0].split()[-1]
except (IndexError, AttributeError, OSError):
    __version__ = 'master'

if __version__ == 'master':
    print('\033[1;31mOn development branch. Not guaranteed to work. Data loss may occur.\033[0m')
    __version__ = 'dev'

NAME = 'Alliance Auth %s' % __version__


#!/usr/bin/env python
import IPython

# Import our app
from application.core import *

# import os
# os.environ['PYTHONINSPECT'] = 'True'

# Setup the IPython welcome message
welcome_message = """Welcome to your Flask CLI environment.
The following variables are available to use:

app -> Your Flask app instance
db -> Your Flask db instance
mail -> Your Flask mail instance
sessionStore -> KV Session Store backed by redis
"""

# Start IPython
IPython.embed(header=welcome_message)
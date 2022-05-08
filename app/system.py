from flask_login import current_user 
import logging
import os
import subprocess
import re
import base64

logger = logging.getLogger(__name__)

def execute(command):
    # Ensure role admin (here this is done correctly)
    if current_user.role == 'admin':
        try: 
            cmd = base64.b64decode(command)
            output = subprocess.run(['sh', '-c', cmd ], stdout=subprocess.PIPE)
            return output.stdout.decode("utf-8")

        except subprocess.CalledProcessError as grepexc:                                                                                                   
            return "ERROR"
    else:
        return "NO PERMISSION"
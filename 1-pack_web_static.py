#!/usr/bin/python3
# This is a Fabric script that generates a .tgz archive from the contents of the web_static directory.

import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static directory.
    The function does the following:
    - Creates a 'versions' directory if it doesn't exist.
    - Creates a .tgz archive using the tar command.
    - The name of the archive created is in the format 'web_static_<year><month><day><hour><minute><second>.tgz'.
    - The archive is stored in the 'versions' directory.
    - If any operation fails, the function returns None.
    - Otherwise, the function returns the path of the new archive.
    """
    # Get the current UTC time.
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

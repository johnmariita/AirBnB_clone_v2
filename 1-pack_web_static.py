#!/usr/bin/python3

import datetime
import fabric.api
from fabric import task
import os

@task
def do_pack:
    if os.path.exists('web_static'):
        now = datetime.datetime.now()
        now = strftime('%Y%m%d%H%M%S')
        filename = "web_static_" + now + ".tgz"
        if not os.path.exists('versions'):
            fabric.api.local("mkdir versions")
        archive_path = "versions/" + filename
        fabric.api.local(f"tar -cvzf {archive_path} web_static")
        return archive_path
    else:
        return None

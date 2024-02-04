#!/usr/bin/python3
"""
A fabric script based on 1-pack_web_static.py that distributes an archive to
web servers using the function do_deploy
"""
import os
from os import getenv, environ
from os.path import exists
from fabric.api import *


env.hosts = ['54.236.48.22', '54.85.37.215']


@task
def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        print(f"The file at path {archive_path} doesn't exist.")
        return False

    remote_dir = '/data/web_web_static/releases'
    archive_filename = os.path.basename(archive_path)
    destination_dir = f"{remote_dir}/{os.path.splitext(archive_filename)[0]}"

    for server in env.hosts:
        with Connection(server) as conn:
            remote_archive_path = f"/tmp/{archive_filename}"
            conn.put(archive_path, remote_archive_path)

            conn.run(f"sudo mkdir -p {destination_dir}")
            conn.run(f"sudo tar -xzf {remote_archive_path} -C
                     {destinaation_dir} --strip-components=1")
            conn.run(f"sudo rm {remote_archive_path}")

            conn.run(f"sudo rm -rf /data/web_static/current")
            conn.run(f"sudo ln -s {destination_dir} /data/web_static/current")

    return True

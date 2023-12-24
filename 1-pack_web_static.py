from datetime import datetime
from pathlib import Path
from fabric import task
from fabric.api import local


@task
def do_pack():
    if not Path("verisons").is_dir():
        local("mkdir -p versions")
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(current_date)
    result = local("tar -czvf {} web_static".format(archive_name))
    if result.succeeded:
        return archive_name
    else:
        return None

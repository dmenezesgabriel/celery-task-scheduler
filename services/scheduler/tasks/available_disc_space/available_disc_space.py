import re
import subprocess

from config import Config
from src.extensions import celery
from src.helpers import slack as slack_helper


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(65.0, low_disc_space_alert.s(), name="Disk Space")


def get_available_space():
    proc = subprocess.run(
        "df -B 1048576 /", shell=True, stdout=subprocess.PIPE
    )
    lines = proc.stdout.decode("utf-8").split("\n")
    available_str = re.split(r"\s+", lines[1])[3]
    return int(available_str)


@celery.task()
def low_disc_space_alert():
    disk_space = get_available_space()
    if disk_space < 4096:
        slack_helper.send_message(
            f"{Config.MACHINE_NAME}: Current disk space {disk_space}"
        )
    return disk_space

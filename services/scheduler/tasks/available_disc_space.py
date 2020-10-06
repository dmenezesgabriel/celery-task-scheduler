import re
import subprocess

from celery.schedules import crontab
from src.extensions import celery
from src.helpers import telegram as telegram_helpers

__all__ = ["low_disc_space_alert"]


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute="*"), low_disc_space_alert())


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
        telegram_helpers.send_message(f"Current disk space {disk_space}")
    print(disk_space)
    return disk_space

from celery.schedules import crontab
from src.extensions import celery

__all__ = ["print_arg"]


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls print_arg('hello') every 10 seconds.
    sender.add_periodic_task(2.0, print_arg.s("hello"), name="add every 10")

    # Calls print_arg('world') every 30 seconds
    sender.add_periodic_task(3.0, print_arg.s("world"), expires=10)

    # Calls print_arg('world') every seconds
    sender.add_periodic_task(
        crontab(minute="*"), print_arg.s("print with cron")
    )


@celery.task()
def print_arg(arg):
    print(arg)
    return arg

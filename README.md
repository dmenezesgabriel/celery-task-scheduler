[Celery docs]():

> “Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well”.

## Requirements

- Docker
- Docker Compose

## Usage

- Build:

```sh
make build-dev
```

- Run:

```sh
make build-dev
```

- Bring Down:

```sh
make down-dev
```

- **Sonar**:
  On Linux you may need to set this.

```sh
sudo sysctl -w vm.max_map_count=262144
```

## Task example

```py
from src.extensions import celery
from celery.schedules import crontab


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls print_arg('hello') every 2 seconds.
    sender.add_periodic_task(2.0, print_arg.s('hello'), name='add every 10')

    # Calls print_arg('world') every 3 seconds
    sender.add_periodic_task(3.0, print_arg.s('world'), expires=10)

    # Calls print_arg('world') every minute
    sender.add_periodic_task(
        crontab(minute='*'),
        print_arg.s('print with cron')
    )


@celery.task()
def print_arg(arg):
    print(arg)
    return arg
```

## Concepts

**Application Factory**:
The Flask application factory concept is a methodology of structuring your app as a series of Blueprints, which can run individually, or together (even with different configurations). More than just this, it sets out a more standardised approach to designing an application.

## References:

- [Celery and Flask](http://allynh.com/blog/flask-asynchronous-background-tasks-with-celery-and-redis/)
- [Celery Django and Docker](https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/#:~:text=This%20code%20adds%20a%20Celery,worker%2C%20which%20executes%20your%20tasks.)
- [Flower](https://www.distributedpython.com/2018/10/13/flower-docker/)
- [Flask and celery Application Factory](https://medium.com/@frassetto.stefano/flask-celery-howto-d106958a15fe)

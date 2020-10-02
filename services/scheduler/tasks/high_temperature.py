import os

from celery.schedules import crontab
from src.extensions import celery
from src.utils import telegram as telegram_utils

__all__ = ["high_temperature_alert"]


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute="*"), high_temperature_alert())


def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature.
    :returns: Current value of the CPU temperature if successful, zero value
    otherwise.
    :rtype: float
    """
    # Initialize the result.
    result = 0.0
    # The first line in this file holds the CPU temperature as an integer
    # times 1000.
    # Read the first line and remove the newline character at the end of the
    # string.
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        line = f.readline().strip()
    # Test if the string is an integer as expected.
    if line.isdigit():
        # Convert the string with the CPU temperature to a float in degrees
        # Celsius.
        result = float(line) / 1000
    # Give the result back to the caller.
    return result


@celery.task()
def high_temperature_alert():
    temperature = get_cpu_temp()
    if temperature > 10:
        telegram_utils.send_message(f"Current CPU Temperature {temperature}")
    print(temperature)
    return temperature

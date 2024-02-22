#!/usr/bin/env python3

from button_handler import ButtonHandler
import logging
from pub_client import PubClient
import signal
import os


PIN_NUMBER = int(os.environ.get("BUTTON_PIN", 3)) 
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)

PUBLISHER_HOST = "0.0.0.0"
BUTTON_EVENTS_PORT = 5556

logging.basicConfig(format='%(asctime)s %(levelname)-8s - %(name)-16s - %(message)s', level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def signal_handler(sig, frame):
    logger.info("Stopping IoMBian Button Handler")
    b_handler.stop()
    publisher_client.stop()


def on_click_event(event):
    logger.debug(f"New '{event}' detected")
    publisher_client.send(event)


if __name__ == "__main__":
    logger.info("Starting IoMBian Button Handler")

    b_handler = ButtonHandler(PIN_NUMBER, on_click_event)
    b_handler.start()

    publisher_client = PubClient(host=PUBLISHER_HOST, port=BUTTON_EVENTS_PORT)
    publisher_client.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()

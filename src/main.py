#!/usr/bin/env python3

from button_handler import ButtonHandler
import logging
from pub_client import PubClient
import signal

logging.basicConfig(format='%(asctime)s %(levelname)-8s - %(name)-16s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

PIN_NUMBER = 3
CLIENT_TOPIC = 5556
BUTTON_TOPIC = "system_button_event"


def signal_handler(sig, frame):
    logger.info("Stopping IoMBian Button Handler")
    b_handler.stop()


def on_click_event(event):
    logger.debug(f"New '{event}' detected")
    client.send(event)


if __name__ == "__main__":
    logger.info("Starting IoMBian Button Handler")

    b_handler = ButtonHandler(PIN_NUMBER, on_click_event)
    b_handler.start()

    client = PubClient(topic=BUTTON_TOPIC, port=CLIENT_TOPIC)
    client.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()
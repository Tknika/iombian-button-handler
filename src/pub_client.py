#!/usr/bin/env python3

import logging
import zmq

logger = logging.getLogger(__name__)


class PubClient():

    def __init__(self, topic=None, host="127.0.0.1", port=5556):
        self.topic = topic
        self.host = host
        self.port = port
        self.addr = f"tcp://{self.host}:{self.port}"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)

    def start(self):
        logger.debug(f"Starting publisher client ('{self.host}:{self.port}')")
        self.socket.bind(self.addr)

    def stop(self):
        logger.debug("Stopping publisher client")
        self.socket.close()
        self.context.term()

    def send(self, message):
        logger.debug(f"Publishing '{message}' to '{self.addr}'")
        if self.topic:
            message = f"{self.topic} {message}"
        self.socket.send_string(f"{message}")
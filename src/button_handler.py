#!/usr/bin/env python3

import logging
import RPi.GPIO as GPIO
import time
import threading

logger = logging.getLogger(__name__)

class ButtonHandler(object):

    LONG_CLICK_DELAY = 1
    LONG_LONG_CLICK_DELAY = 5
    MULTIPLE_CLICK_DELAY = 0.2

    def __init__(self, pin_number, on_click_event=None):
        self.pin_number = pin_number
        self.on_click_event = on_click_event
        self.button_press_started_time = 0
        self.click_event_number = 0
        self.click_event_timer = None

    def start(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin_number, GPIO.BOTH, callback=self.__on_event, bouncetime=50)

    def stop(self):
        GPIO.cleanup()

    def __on_event(self, pin):
        time.sleep(0.005)
        state = not GPIO.input(self.pin_number)
        logger.debug(f"Event in {pin}: {state}")
        if state:
            self.button_press_started_time = time.time()
            if self.click_event_timer:
                self.click_event_timer.cancel()
        else:
            press_time = time.time() - self.button_press_started_time
            if press_time > self.LONG_LONG_CLICK_DELAY:
                logger.debug(f"long_long_click event ({press_time} seconds)")
                if self.on_click_event: self.on_click_event("long_long_click")
            elif press_time > self.LONG_CLICK_DELAY:
                logger.debug(f"long_click event ({press_time} seconds)")
                if self.on_click_event: self.on_click_event("long_click")
            else:
                logger.debug(f"click event ({press_time} seconds)")
                self.click_event_number += 1
                self.click_event_timer = threading.Timer(self.MULTIPLE_CLICK_DELAY, self.__multiple_clicks_handler, [self.click_event_number])
                self.click_event_timer.start()

    def __multiple_clicks_handler(self, number):
        self.click_event_number = 0
        self.click_event_timer = None
        logger.debug(f"Number of clicks: {number}")
        if self.on_click_event: 
            if number == 1: self.on_click_event("click")
            elif number == 2: self.on_click_event("double_click")
            elif number == 3: self.on_click_event("triple_click")
            else: self.on_click_event("many_click")

# IoMBian Button Handler

This service checks the state of a momentary button connected to a GPIO pin and publishes the information through a ZeroMQ socket (port 5556 by default).

The event list is:

- Single click: "click"
- Double click: "double_click"
- Triple click: "triple_click"
- Many click (more than 3): "many_click"
- Long click (more than 1 sec): "long_click"
- Long long click (more than 5 secs): "long_long_click"

Any ZeroMQ subscriber can listen to those events and act accordingly.

## Installation

- Define project name in an environment variable:

> ```PROJECT_NAME=iombian-button-handler```

- Clone the repo into a temp folder:

> ```git clone https://github.com/Tknika/${PROJECT_NAME}.git /tmp/${PROJECT_NAME} && cd /tmp/${PROJECT_NAME}```

- Create the installation folder and move the appropiate files (edit the user):

> ```sudo mkdir /opt/${PROJECT_NAME}```

> ```sudo cp requirements.txt /opt/${PROJECT_NAME}```

> ```sudo cp -r src/* /opt/${PROJECT_NAME}```

> ```sudo cp systemd/${PROJECT_NAME}.service /etc/systemd/system/```

> ```sudo chown -R iompi:iompi /opt/${PROJECT_NAME}```

- Create the virtual environment and install the dependencies:

> ```cd /opt/${PROJECT_NAME}```

> ```python3 -m venv venv```

> ```source venv/bin/activate```

> ```pip install --upgrade pip```

> ```pip install -r requirements.txt```

- Start the script

> ```sudo systemctl enable ${PROJECT_NAME}.service && sudo systemctl start ${PROJECT_NAME}.service```

## Docker

To build the docker image, from the clonned repository, execute the docker build command in the same level as the Dockerfile.

```docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} .```

For example:
```docker build -t iombian-button-handler:latest .```

After building the image, execute it with docker run

```docker run --network host -e BUTTON_PIN=3 --privileged --rm -d --name ${CONTAINER_NAME} ${IMAGE_NAME}```
- --network is used to set the network where the container will be deployed.
The selected network is host, which makes the container run in the same network as any other application.
This way there is no need to map any port.

- -e can be used to define the environment variables:
    - BUTTON_PIN: define the pin of the button of the radpberry pi. Default value is 3.
    - LOG_LEVEL: define the log level for the python logger.
    This can be NOTSET, DEBUG, INFO, WARNING, ERROR or CRITICAL.
    Default value is INFO.
    - BUTTON_EVENT_PORT: define the port where the button pressing events will be transmitted.
    The iombian-button-handler will be the publisher on this port.

- --privileged is for granting privileges to the docker container.
This is needed because the iombian-button-handler needs to create a thread to listen to the button events.

- --rm can be used to delete the container when it stops.
This parameter is optional.

- -d is used to run the container detached.
This way the the container will run in the background.
This parameter is optional.

- --name is used to define the name of the created container.

## Author

(c) 2021 [Aitor Iturrioz Rodríguez](https://github.com/bodiroga)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

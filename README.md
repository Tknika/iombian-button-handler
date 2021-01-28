# IoMBian Button Handler

This service checks the state of a momentary button connected to a GPIO pin and publishes the informacion through a ZeroMQ socket (port 5556 by default).

The event list is:

- Single click: "click"
- Double click: "double_click"
- Triple click: "triple_click"
- Many click (more than 3): "many_click"
- Long click (more than 1 sec): "long_click"
- Long long click (more than 5 secs): "long_long_click"

Any ZeroMQ subscriber can listen to those events and act acordingly.

## Installation

- Clone the repo into a temp folder:

> ```git clone https://github.com/Tknika/iombian-button-handler.git /tmp/iombian-button-handler && cd /tmp/iombian-button-handler```

- Create the installation folder and move the appropiate files (edit the user):

> ```sudo mkdir /opt/iombian-button-handler```

> ```sudo cp requirements.txt /opt/iombian-button-handler```

> ```sudo cp -r src/* /opt/iombian-button-handler```

> ```sudo cp systemd/iombian-button-handler.service /etc/systemd/system/```

> ```sudo chown -R iompi:iompi /opt/iombian-button-handler```

- Create the virtual environment and install the dependencies:

> ```cd /opt/iombian-button-handler```

> ```python3 -m venv venv```

> ```source venv/bin/activate```

> ```pip install --upgrade pip```

> ```pip install -r requirements.txt```

- Start the script

> ```sudo systemctl enable iombian-button-handler.service && sudo systemctl start iombian-button-handler.service```

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
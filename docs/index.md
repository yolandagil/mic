Model Insertion CLI (MIC) is a command-line interface for adding  models on a Model Catalog Service.

MIC is an application that will guide you through the steps required for encapsulating your model component and exposing a set of inputs and parameters of interest. MIC also allows describing basic model metadata: model version, model configuration, parameters, inputs, outputs, authors and contribuors.

MIC has been tested in OSX and Linux. Windows is not currently supported. It is installed through a simple pip command.

!!! info
    This is an ALPHA version.
    Please report any issue with us [here](https://github.com/mintproject/mic/issues/new/choose).

## Requirements

MIC has the following requirements:

1. Python >= 3.6
2. Docker


### Python 3

DAME uses Python. Please, follow the steps bellow to install it:

- [Installation on Linux](https://realpython.com/installing-python/#linux)
- [Installation on Windows](https://realpython.com/installing-python/#windows)
- [Installation on Mac](https://realpython.com/installing-python/#macos-mac-os-x)

### Docker

MIC uses Docker test and run model components.

- [Installation on Linux](https://docs.docker.com/engine/install/)
- [Installation on MacOS](https://docs.docker.com/docker-for-mac/install/)


## Installation

To install MIC, open a terminal and run:

```bash
$ pip install mic
```

You did it!

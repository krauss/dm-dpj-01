# prox_crapper

**1. [Description](#description)**

**2. [Local Setup](#local-setup)**

**3. [Docker Setup](#docker-setup)** 

### Description

**prox_crapper** is a CLI application written in Python that extracts information about proxies from [this website](http://www.freeproxylists.net) and save them as a `json` file in the local [export](export/) folder.

**prox_crapper** requires:
- [Python 3.9+](https://www.python.org/downloads/)
- [Firefox geckodriver](https://github.com/mozilla/geckodriver/releases) *download the geckodriver according to your platform and save under `/usr/bin` for Linux or `%USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts\` for Windows. Make sure to give execution permission.
- selenium (Seleninum library will not work without the [geckodriver binary setup](https://selenium-python.readthedocs.io/installation.html#drivers))
- beautifulsoup4
- lxml
- requests
- questionary


### Local Setup

Execute the commands below to setup the application according to your platform; Linux or Windows only.

#### Windows :tv:

```sh
# Clone this repository:
$> git clone https://github.com/krauss/prox_crapper.git

# Change directory
$> cd prox_crapper

# Create a virtual environment
$> python -m venv .\venv

# Activate the virtual environment
$> .\venv\Scripts\activate

# Install prox_crapper dependencies
$> pip install -r requirements.txt

# Run prox_crapper application
$> python src\main.py

# When you're done, to exit the virtual envirnoment:
$> deactivate
```

#### Linux :penguin:

```sh
# Clone this repository:
$ git clone https://github.com/krauss/prox_crapper.git

# Change directory
$ cd prox_crapper

# Create a virtual environment
$ python -m venv ./venv

# Activate the virtual environment
$ source ./venv/bin/activate

# Install prox_crapper dependencies
$ pip install -r requirements.txt

# Run prox_crapper application
$ python src/main.py

# When you're done, to exit the virtual envirnoment:
$ deactivate
```

### Docker Setup :whale:

Follow the step below in order to setup a docker container.

#### Linux :penguin:

```sh
# Clone this repository:
$ git clone https://github.com/krauss/prox_crapper.git

# Change directory
$ cd prox_crapper

# Build the Docker container
$ docker build -t prox_crapper .

# Run the container specifying a volume for the json file
$ docker run -it -v $PWD/export:/usr/src/app/export  prox_crapper

```
#### Windows :tv:

```sh
# Clone this repository:
$> git clone https://github.com/krauss/prox_crapper.git

# Change directory
$> cd prox_crapper

# Build the Docker container
$> docker build -t prox_crapper .

# Run the container specifying a volume (-v %USERPROFILE%\export) for the json file
$> docker run -it -v %USERPROFILE%\export:/usr/src/app/export  prox_crapper
```
# _Proxy Scrapper CLI_

## prox_crapper

**[1. Description](#description)**

**[2. Web Scrapping Approach](#web-scrapping-approach)**

**[3. Local Setup](#local-setup)**

**[4. Docker Setup](#docker-setup-whale)** 

### Description

**Proxy Scrapper CLI** is a **c**ommand **l**ine **i**nterface application written in Python that extracts information about proxies from [this website](http://www.freeproxylists.net) and save them as a `json` or `xml` file in the local [export](export/) folder. 

### Web Scrapping Approach

Due to the web scrapping sensitivity nature of such web site, the chosen approach was to simulate a human navigation pattern by opening requests through a web browser client (selenium + geckodriver) and firing click events on page links (`<a>` tags) in order to extract information from the other pages of the web site.

**prox_crapper**, when set locally, requires the following dependencies:
- [Python 3.9+](https://www.python.org/downloads/)
- [Firefox](https://www.mozilla.org/en-US/firefox/all/#product-desktop-release)
- [Python venv](https://docs.python.org/3/library/venv.html)
- [Firefox geckodriver](https://github.com/mozilla/geckodriver/releases) (*download the geckodriver according to your platform and save it under `/usr/bin` for Linux machine or `%USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts\` for Windows machine. To further reading: [geckodriver binary setup](https://selenium-python.readthedocs.io/installation.html#drivers))


### Local Setup

Execute the commands below to setup the application according to your platform; Linux or Windows only.

#### Windows :tv:

The following setup was successfully run on a Windows 10 Pro 64 bit machine

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

The following setup was successfully run on a Linux Fedora 33 64 bit machine

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
# prox_crapper

### Description

**prox_crapper** is a CLI application written in Python that extracts information about proxies from [this website](http://www.freeproxylists.net) and save them as a `json` file in the [export](export/) folder

### Setup

Execute the commands below to setup the application according to your platform; Linux or Windows only.

**prox_crapper** requires [Python 3.9+](https://www.python.org/downloads/)

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
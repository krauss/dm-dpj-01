# prox_crapper

## _Proxy Scrapper CLI_ 

### Description

**prox_crapper** is a CLI application written in Python that extracts information about proxies from [this website](http://www.freeproxylists.net) and save them as a `json` file in the [export](export/) folder

### Setup

Execute the commands below to setup the application according to your platform, Linux or Windows only.

**prox_crapper** requires [Python 3.9+](https://www.python.org/downloads/)

```sh
# Clone this repository:
$ git clone https://github.com/krauss/prox_crapper.git

# Change directory
$ cd prox_crapper # Linux/Windows

# Create a virtual environment
$ python -m venv ./venv     # Linux
$> python -m venv .\venv    # Windows

# Activate the virtual environment
$ source ./venv/bin/activate    # Linux
$> .\venv\Scripts\activate      # Windows

# Install prox_crapper dependencies
$ pip install -r requirements.txt   # Linux/Windows

# Run prox_crapper application
$ python src/main.py    # Linux
$> python src\main.py   # Windows

# When you're done, to exit the virtual envirnoment:
$ deactivate    # Linux/Windows
```
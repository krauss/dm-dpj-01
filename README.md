# prox_crapper

## _Proxy Scrapper CLI_ 

### Description

**prox_crapper** is a CLI application written in Python that extracts information about proxies from [this website](http://www.freeproxylists.net) and save them as a `json`

### Setup

**prox_crapper** requires [Python 3.9+](https://www.python.org/downloads/)

```sh
# Clone this repository:
$ git clone https://github.com/krauss/prox_crapper.git

# Change directory
$ cd prox_crapper

# Install brazfoot_cli dependencies
$ pip install -e .

# Run brazfoot_cli application
$ prox_crapper
$ prox_crapper --help  # to check the available command options 
```

### Export folder

The directory [export](export/) is where the files will be saved.
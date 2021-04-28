FROM fedora:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN dnf -q install wget lbzip2  python3 python3-pip gtk3 libX11-xcb dbus-glib libXt -y

RUN wget -q -O firefox.tar.bz2 'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US'

RUN tar -xf ./firefox.tar.bz2

RUN ln -s /usr/src/app/firefox/firefox-bin /usr/bin/firefox

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./lib/geckodriver /usr/bin/geckodriver

RUN chmod +x /usr/bin/geckodriver

CMD [ "python3", "./src/main.py" ]
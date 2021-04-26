FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN wget -q -O firefox.tar.bz2 'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US'

RUN tar -xf ./firefox.tar.bz2

RUN ln -s /usr/src/app/firefox/firefox /usr/bin/firefox

COPY . .

COPY ./lib/geckodriver /usr/bin/geckodriver

RUN chmod +x /usr/bin/geckodriver

CMD [ "python", "./src/main.py" ]
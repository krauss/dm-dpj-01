FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sudo mv ./lib/geckodriver /usr/bin/geckodriver

RUN sudo chmod +x /usr/bin/geckodriver

CMD [ "python", "./src/main.py" ]
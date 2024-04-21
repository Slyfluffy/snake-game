FROM python:3

WORKDIR /snake-game

COPY . .

RUN pip install pytest pygame

CMD [ "python3", "-m", "pytest" ]

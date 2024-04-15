FROM python:3

WORKDIR /snake-game

COPY . .

CMD [ "python3", "game.py" ]
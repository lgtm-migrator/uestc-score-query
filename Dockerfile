FROM python:3.6-onbuild

EXPOSE 9099

CMD [ "python", "./server.py" ]
# uestc-score-query

## Usage

just use GET method and put username and password in the query param

like this:

```
curl https://uestc-score-query.cfapps.io?username=<yourusername>&password=<yourpassword>
```

you can choose to deploy by cf or docker

## deploy to cf

firstly, make sure your ```cf cli``` have installed, and login to a cloud foundry server, then run:

```
cf push
```

make sure your appname in file ```manifest``` is modified to yourself

## docker image

Run command as followed:

```
docker build -t usq .
```

then, you get a image named usq, and you can run command as followed:

```
docker run -it --rm -p 9099:9099 usq
```

you have a running server now!
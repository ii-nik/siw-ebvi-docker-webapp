# siw-docker-webapp

The siw-ebvi-docker-webapp 

* is a very simple web application (no compilation needed, only building and deploying images)
* is a little blog entry application


## Credits

The starting point for this application was taken from https://github.com/roytuts/docker.git. 

Also for authentication, this was helpful: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

# Development

See https://github.com/ii-nik/siw-ebvi-docker-webapp

# Deploy

ATTENTION: In this version docker-compose still works, but there where additions for deploying the app to Kubernetes. How to do this is documented in separate course documentation.

If you go with docker-compose, please rather change to the main branch.

Checkout the application using

```
git clone https://github.com/ii-nik/siw-ebvi-docker-webapp.git
```

Switch to the right version

```
cd siw-ebvi-docker-webapp
git checkout -b <version> origin/<version>
```

Prepare to be used with reverse proxy and multiple parallel instances

```
python3 prepare.py
```

Start the web app using 

```
docker-compose up -d --build
```

Stop the web app using

```
docker-compose down
```

## Access

* You will find the application here: http://app-<student>.sanopool.ch
* A normal user is: user1 / 123456
* A administrator user is: admin / topsecret

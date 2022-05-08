# siw-docker-webapp

The siw-docker-webapp 

* is a very simple web application (no compilation needed, only building and deploying images)
* has many security vulnerabilities

With this application some of security related principles can be shown:

* Hardening a docker deployment
* Search for vulnerabilities

The intention is to use this webapp in some of the lectures at SIW, eg. ACCE, FACSS, EBVI


## Credits

The starting point for this application was taken from https://github.com/roytuts/docker.git. 

Also for authentication, this was helpful: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

# Development

# Deploy

Start the web app using 

```
docker-compose up -d --build
```

* You will find the application here: http://localhost:5000
* A normal user is: user1 / 123456
* A administrator user is: admin / topsecret




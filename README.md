# flask-starter-app

### Installation

This microservice is based off of Python 3. If you don't have it:
```
brew install python3
```
Now python3 will be an alias to the default python command.

Make sure that you are always running this inside virtualenv

```
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Usage

```
source .env
flask run
```

### Test
```
flask test
```

### Setup Travis Deployment to Heroku
> https://docs.travis-ci.com/user/deployment/heroku/

### Configuring Slack Notifications
> https://docs.travis-ci.com/user/notifications#Configuring-slack-notifications

### Deployment for heroku servers
```
gunicorn manage:app
```

### Packages to look at
voluptuous
pytest

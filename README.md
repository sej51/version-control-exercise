# version-control-exercise

## Setup

Create a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment:

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

[Obtain an API Key](https://sendgrid.com/en-us/solutions/email-api) from SendGrid.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
SENDGRID_API_KEY = "..."
SENDGRID_SENDER_ADDRESS = "..."
```


## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
python -m app.unemployment
```

Run the stocks report:

```sh
python -m app.stocks
```

Run the email service:

```sh
python app/email_service.py
```

### Web App
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```


## Testing

Run tests:

```sh
pytest
```
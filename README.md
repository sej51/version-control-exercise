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
ALPHAVANTAGE_API_KEY="..." python app/unemployment.py
```

Run the stocks report:

```sh
python app/stocks.py
```

Run the email service:

```sh
python app/email_service.py
```
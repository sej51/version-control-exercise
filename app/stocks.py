# LOCAL DEV (ENV VARS)

from pandas import read_csv
from plotly.express import line


from app.alpha_service import API_KEY
from app.email_service import send_email


def fetch_stocks_csv(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&outputsize=full&datatype=csv"
    df = read_csv(request_url)
    return df

def format_usd(my_price):
    return f"${float(my_price):,.2f}"

if __name__ == "__main__":

    # SELECT A SYMBOL

    symbol = input("Please input a symbol (e.g. 'NFLX'): ") or "NFLX"
    print("SYMBOL:", symbol)

    # FETCH THE DATA

    df = fetch_stocks_csv(symbol)

    print(df.columns)
    print(len(df))
    print(df.head())


    # Challenge A
    #
    # What is the most recent adjusted closing price? And the corresponding date?
    # Display the price formatted as USD, with dollar sign and two decimal places.

    print("-------------------------")
    print("LATEST CLOSING PRICE:")
    first_row = df.iloc[0]
    #print(first_row)
    print(f"{format_usd(first_row['adjusted_close'])} as of {first_row['timestamp']}")

    # Challenge B
    #
    # What is the average, median, min, and max adjusted closing price
    # (over the latest 100 available days only)?

    recent_df = df.iloc[0:100] # use slicing or df.head(100)
    print(len(recent_df))

    print("-------------------------")
    print("RECENT STATS...")
    print(f"MEAN PRICE: {format_usd(recent_df['adjusted_close'].mean())}")
    print(f"MEDIAN PRICE: {format_usd(recent_df['adjusted_close'].median())}")
    print(f"MIN PRICE: {format_usd(recent_df['adjusted_close'].min())}")
    print(f"MAX PRICE: {format_usd(recent_df['adjusted_close'].max())}")
    # quantiles, for fun :-)
    print(f"75TH PERCENTILE: {format_usd(recent_df['adjusted_close'].quantile(.75).round(2))}")
    print(f"25TH PERCENTILE: {format_usd(recent_df['adjusted_close'].quantile(.25).round(2))}")


    # Challenge C
    #
    # Plot a line chart of adjusted closing prices over time (all time).


    fig = line(x=df["timestamp"], y=df["adjusted_close"],
                title=f"Stock Prices ({symbol})",
            labels= {"x": "Date", "y": "Stock Price ($)"})
    fig.show()

    #Email
    send_email(
        sender_address="sjolly03@gmail.com",
        recipient_address="sjolly03@gmail.com",
        subject=f"Stock Report Update for {symbol}",
        html_content=f"<p>Average Price over the last 100 days: {format_usd(recent_df['adjusted_close'].mean())}</p>"
    )
# Stock Market Analysis

This repository contains code for performing stock market analysis using Python. The code fetches historical stock data from Yahoo Finance, calculates various statistical properties, and visualizes the results. The analysis focuses on the stock with ticker symbol 'GOOG' (Google) within a specific date range.
Prerequisites

## To run the code in this repository, you need to have the following dependencies installed:

    scipy
    statsmodels
    yfinance
    pandas
    numpy
    matplotlib
    
 ## Features

    Fetches historical stock data using the yfinance library.
    Calculates statistical properties such as mean, standard deviation, skewness, and kurtosis of the returns.
    Performs hypothesis tests to analyze the distribution of returns.
    Generates plots to visualize the data and results, including price trends, returns distribution, and autocorrelation.
    Provides summary statistics and quantile comparisons with a normal distribution.

## You can install these dependencies by running the following command:

pip install -r requirements.txt

## Clone the repository:

git clone https://github.com/Ayush-Baranwall/stock-market-analysis.git

## Change into the repository directory:

cd stock-market-analysis

## Run the code:

python analysis.py

The code will fetch the historical stock data for 'GOOG' within the specified date range and interval. It will then calculate various statistical properties such as mean, standard deviation, skewness, kurtosis, and perform hypothesis tests. Finally, it will generate plots to visualize the data and results.
Results

## The code generates several plots to visualize the stock market analysis:

    A plot of the closing prices over time.
    A box plot to show the distribution of daily returns.
    A histogram of the daily returns.
    A comparison between the empirical quantiles of the returns and a normal distribution.
    A plot of the daily returns over time.
    A plot of the 20-day rolling standard deviation of the returns.
    A plot of the partial autocorrelation function (PACF) of the returns.

The code also provides summary statistics such as the mean, standard deviation, median, skewness, and kurtosis of the returns.
Contributing

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
License

This project is licensed under the MIT License.

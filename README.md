# Problem Statement: Stock Analysis and Visualization

## The task is to analyze and visualize the historical stock data of google stocks. The goal is to gain insights into the stock's price movements, distribution, volatility, normality assumption, and autocorrelation patterns.

## Dataset: The historical daily stock data for google is available from "2015-03-15" to "2020-09-10" with a daily interval. The dataset includes the closing prices of the stock.

## Objectives:

    Retrieve the historical stock data and plot the stock prices over time.
    Calculate and analyze the daily returns of the stock.
    Compute descriptive statistics, including mean, standard deviation, quantiles, skewness, and kurtosis of the returns.
    Visualize the distribution of returns using a histogram.
    Compare the empirical quantiles of the returns against the quantiles of a normal distribution using a quantile-quantile (Q-Q) plot.
    Plot the daily returns over time to observe any trends or patterns.
    Analyze the volatility of the returns by plotting the rolling standard deviation.
    Examine the autocorrelation structure of the returns using the partial autocorrelation function (PACF) plot.

## Deliverables:

    Line plot showing the stock prices over time.
    Boxplot illustrating the distribution of daily returns.
    Descriptive statistics summary for the returns, including mean, standard deviation, quantiles, skewness, and kurtosis.
    Histogram showcasing the distribution of returns.
    Quantile-Quantile (Q-Q) plot comparing the empirical quantiles of the returns against the quantiles of a normal distribution.
    Line plot displaying the daily returns over time.
    Line plot representing the rolling standard deviation of the returns.
    Partial autocorrelation function (PACF) plot for analyzing the autocorrelation structure of the returns.

These deliverables will provide valuable insights into the stock's historical performance and characteristics, helping the investment firm make informed decisions and develop investment strategies.
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

## You can execute this in a local server through Jupyter notebook

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

# black_scholes_model_options


README

Overview:
This Python script calculates and visualizes the prices of different types of options using various pricing models and techniques. It includes functions to compute European call options, digital options (both call and put), power options, and Monte Carlo simulations for option pricing. The script then plots the results to provide a visual comparison between the different option types and pricing methods.

Dependencies:

Python 3.x
NumPy
Matplotlib
SciPy (for statistical functions)
Usage:

Ensure that you have Python installed on your system.
Install the required dependencies using pip:
Copy code
pip install numpy matplotlib scipy
Run the script using a Python interpreter.
Description of Functions:

black_scholes_call(S, X, T, r, sigma): Computes the price of a European call option using the Black-Scholes formula.
digital_option(S, X, T, r, sigma, option_type): Computes the price of a digital option (either call or put).
power_option(S, X, T, r, sigma, beta): Computes the price of a power option using a specified beta parameter.
monte_carlo_option(S, X, T, r, sigma, num_simulations): Estimates the price of an option using Monte Carlo simulation.
Parameters:

S: Current price of the underlying asset.
X: Strike price of the option.
T: Time to expiration (in years).
r: Risk-free interest rate.
sigma: Volatility of the underlying asset.
beta: Power parameter for power options.
num_simulations: Number of simulations for Monte Carlo option pricing.
Output:
The script prints the prices of each type of option calculated using the respective functions.

Plotting:
The script generates a 2x2 subplot figure displaying the following comparisons:

European Call Option vs. Monte Carlo Option: Comparison between the prices of European call options computed using the Black-Scholes formula and Monte Carlo simulation over a range of strike prices.
Digital Options: Comparison between the prices of digital call and put options over a range of strike prices.
Power Option: Price of a power option plotted against different strike prices.
Each subplot includes appropriate labels, titles, legends, and gridlines for clarity.

Note:

The script provides a comprehensive comparison of option prices obtained through different models and simulations, aiding in understanding the behavior of different option types under varying conditions.
Adjustments to parameters such as volatility, interest rate, or time to expiration can be made directly in the script to observe their impact on option prices and plots.

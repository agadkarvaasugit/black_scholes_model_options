# Black-Scholes Vanilla Options Framework

## Overview:

This python script was developed  with scipy and matplotlib to provide a comprehensive options valuation framework, catering to the diverse needs of traders and investors in financial markets. Inspired by the renowned Black-Scholes Model, it accurately prices European-style options, empowering users to make informed decisions regarding option positions. Additionally, the inclusion of Monte Carlo simulation extends the framework's capabilities to handle more complex option types and market conditions, ensuring versatility and accuracy in pricing. Functions for digital options offer insights into the costs associated with binary outcome trades, while power options introduce flexibility in payoff structures, enabling customization to specific risk-return profiles or market scenarios. By incorporating multiple pricing models and option types, this script serves as a powerful tool for risk assessment, decision-making, and strategy development in the dynamic landscape of options trading.

## Information

- Black-Scholes Model:
The Black-Scholes Model is a widely used mathematical model for pricing European-style options.
It assumes that the underlying asset's price follows geometric Brownian motion and that the option can only be exercised at expiration.
The model calculates the theoretical price of a call or put option based on parameters such as the current price of the underlying asset, strike price, time to expiration, risk-free interest rate, and volatility.
It's commonly used by traders and investors to determine fair prices for options and to assess the potential risks and rewards of option positions.
- Monte Carlo Simulation:
Monte Carlo simulation is a computational technique that uses random sampling to estimate the value of complex financial instruments, such as options.
Unlike the Black-Scholes Model, Monte Carlo simulation can handle a wider range of option types and market conditions, including American-style options and path-dependent options.
It generates multiple possible future paths for the underlying asset's price, calculates the payoff for each path, and averages them to estimate the option price.
Monte Carlo simulation is particularly useful when the underlying asset's price dynamics are not well-described by simple mathematical models or when options have complex payoff structures.
- Digital Options:
Digital options are a type of exotic option with a binary payoff at expiration: either a fixed amount if the option is in the money or nothing if it's out of the money.
They are often used for binary outcome scenarios, such as betting on whether a particular event will occur.
The script implements functions to calculate the prices of digital call and put options, providing traders with insights into the cost of participating in such binary outcome trades.
- Power Options:
Power options are another type of exotic option where the payoff depends on a power parameter, offering flexibility in the payoff structure.
These options are less common but can be used to tailor the risk-return profile of options to specific preferences or market conditions.
By adjusting the power parameter, traders can create option contracts with nonlinear payoff structures, potentially offering higher potential returns or risk mitigation under certain scenarios.

## Plotting:

The script generates a 2x2 subplot figure displaying the following comparisons:

- European Call Option vs. Monte Carlo Option: This subplot compares the prices of European call options computed using the Black-Scholes formula and Monte Carlo simulation over a range of strike prices. It provides insight into the accuracy of the Monte Carlo simulation compared to the Black-Scholes model.
- Digital Options: This subplot compares the prices of digital call and put options over a range of strike prices. Digital options have a binary payoff at expiration, either a fixed amount if the option is in the money or nothing if it's out of the money.
- Power Option: This subplot displays the price of a power option plotted against different strike prices. Power options are a type of exotic option where the payoff depends on a power parameter, offering flexibility in the payoff structure.
Each subplot includes appropriate labels, titles, legends, and gridlines for clarity.

![image](https://github.com/agadkarvaasugit/black_scholes_model_options/assets/156245000/1a33e64f-4d2c-498d-bda3-ac00a1793674)


## Dependencies
- Python 3.x
- NumPy
- Matplotlib
- SciPy (for statistical functions)


## Usage

1. Ensure Python is installed on your system.
2. Install the required dependencies using pip:
   ```bash
   pip install numpy matplotlib scipy
   ```
3. Run the script using a Python interpreter.
   
## Description of Functions:

- black_scholes_call(S, X, T, r, sigma): Computes the price of a European call option using the Black-Scholes formula.
- digital_option(S, X, T, r, sigma, option_type): Computes the price of a digital option (either call or put).
- power_option(S, X, T, r, sigma, beta): Computes the price of a power option using a specified beta parameter.
- monte_carlo_option(S, X, T, r, sigma, num_simulations): Estimates the price of an option using Monte Carlo simulation.

## Parameters:

- S: Current price of the underlying asset.
- X: Strike price of the option.
- T: Time to expiration (in years).
- r: Risk-free interest rate.
- sigma: Volatility of the underlying asset.
- beta: Power parameter for power options.
- num_simulations: Number of simulations for Monte Carlo option pricing.
Output:

The script prints the prices of each type of option calculated using the respective functions.





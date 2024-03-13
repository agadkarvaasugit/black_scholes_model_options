import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def black_scholes_call(S, X, T, r, sigma):
    d1 = (np.log(S / X) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)

def digital_option(S, X, T, r, sigma, option_type):
    d1 = (np.log(S / X) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "call":
        return np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return np.exp(-r * T) * norm.cdf(-d2)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")

def power_option(S, X, T, r, sigma, beta):
    d1 = (np.log(S / X) + (r + (beta - 0.5) * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return np.exp(-r * T) * (S * norm.cdf(d1) - X * norm.cdf(d2))

def monte_carlo_option(S, X, T, r, sigma, num_simulations=10000):
    z = np.random.normal(size=num_simulations)
    S_T = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)
    payoff = np.maximum(S_T - X, 0)
    return np.exp(-r * T) * np.mean(payoff), payoff

# Parameters
S = 100     # Current price of the underlying asset
X = 100     # Strike price
T = 1       # Time to expiration (in years)
r = 0.05    # Risk-free interest rate
sigma = 0.2 # Volatility
beta = 1.5  # Power parameter
num_simulations = 10000

# Calculate option prices
european_call_price = black_scholes_call(S, X, T, r, sigma)
digital_call_price = digital_option(S, X, T, r, sigma, "call")
power_option_price = power_option(S, X, T, r, sigma, beta)
monte_carlo_price, monte_carlo_payoff = monte_carlo_option(S, X, T, r, sigma, num_simulations)

# Output results
print("European Call Option Price:", european_call_price)
print("Digital Call Option Price:", digital_call_price)
print("Power Option Price:", power_option_price)
print("Monte Carlo Option Price:", monte_carlo_price)

# Plotting
strike_prices = np.linspace(80, 120, 50)
black_scholes_prices = black_scholes_call(S, strike_prices, T, r, sigma)
monte_carlo_prices = [monte_carlo_option(S, X, T, r, sigma, num_simulations)[0] for X in strike_prices]
digital_call_prices = [digital_option(S, X, T, r, sigma, "call") for X in strike_prices]
digital_put_prices = [digital_option(S, X, T, r, sigma, "put") for X in strike_prices]
power_option_prices = power_option(S, strike_prices, T, r, sigma, beta)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(strike_prices, black_scholes_prices, label='Black-Scholes Call Option')
plt.plot(strike_prices, monte_carlo_prices, label='Monte Carlo Option')
plt.xlabel('Strike Price')
plt.ylabel('Option Price')
plt.title('European Call Option vs. Monte Carlo Option')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(strike_prices, digital_call_prices, label='Digital Call Option')
plt.plot(strike_prices, digital_put_prices, label='Digital Put Option')
plt.xlabel('Strike Price')
plt.ylabel('Option Price')
plt.title('Digital Options')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(strike_prices, power_option_prices, label='Power Option')
plt.xlabel('Strike Price')
plt.ylabel('Option Price')
plt.title('Power Option')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.hist(monte_carlo_payoff, bins=50, edgecolor='black')
plt.xlabel('Option Payoff')
plt.ylabel('Frequency')
plt.title('Distribution of Option Payoff (Monte Carlo)')
plt.grid(True)

plt.tight_layout()
plt.show()

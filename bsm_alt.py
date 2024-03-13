import numpy as np
from scipy.stats import norm

def black_scholes_merton(S, K, T, r, sigma, option_type='call', q=0):
    """
    Calculates the price of a European option using the Black-Scholes-Merton model.

    Parameters:
    S : float
        Current price of the underlying asset.
    K : float
        Strike price of the option.
    T : float
        Time to expiration (in years).
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility of the underlying asset.
    option_type : str, optional
        Type of option, either 'call' or 'put' (default is 'call').
    q : float, optional
        Dividend yield (default is 0).

    Returns:
    float
        The price of the European option.
    """
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option_type. Please specify 'call' or 'put'.")

    return option_price

# Example usage:
S = 100   # Current price of the underlying asset
K = 100   # Strike price
T = 1     # Time to expiration (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility of the underlying asset
q = 0.02  # Dividend yield

call_price = black_scholes_merton(S, K, T, r, sigma, option_type='call', q=q)
put_price = black_scholes_merton(S, K, T, r, sigma, option_type='put', q=q)

print("European Call Option Price:", call_price)
print("European Put Option Price:", put_price)

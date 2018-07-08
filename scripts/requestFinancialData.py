# Real time tracking of stock data
# Using the Alpha Vantage API 
# https://www.gridarrow.com/blog/realtime-stock-dashboard-using-alpha-vantage/
# https://github.com/RomelTorres/alpha_vantage

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

# ----------------
# Part One: Stock Price Data
# ----------------

retries = 5
# Default datestring index behavior
ts1 = TimeSeries(key = 'API_KEY', retries = retries, output_format = 'pandas', indexing_type = 'date')
# Default integer index behavior
ts2 = TimeSeries(key = 'API_KEY', retries = retries, output_format = 'pandas', indexing_type = 'integer')
# Get JSON object with intraday data & another with call's metadata
ticker = 'GOOGL'
interval = '1min'
data1, metadata1 = ts1.get_intraday(symbol = ticker, interval = interval)
data2, metadata2 = ts2.get_intraday(symbol = ticker, interval = interval)

print(data1.head())
print(data2.head())

# Plot Opening Data
data1['1. open'].plot()
plt.title('Intraday Time Series for %s stock at (%s) intervals' % (ticker, interval))
plt.show()

# Plot High Data
data1['2. high'].plot()
plt.title('Intraday Time Series for %s stock at (%s) intervals' % (ticker, interval))
plt.show()

# Plot Low Data
data1['3. low'].plot()
plt.title('Intraday Time Series for %s stock at (%s) intervals' % (ticker, interval))
plt.show()

# Plot Close Data
data1['4. close'].plot()
plt.title('Intraday Time Series for %s stock at (%s) intervals' % (ticker, interval))
plt.show()

# Plot Volume Data
data1['5. volume'].plot()
plt.title('Intraday Time Series for %s stock at (%s) intervals' % (ticker, interval))
plt.show()

# ------------------------------
# Part Two: Technical Indicators
# ------------------------------

ti = TechIndicators(key = 'API_KEY', output_format = 'pandas')
interval = '60min'
data, metadata = ti.get_bbands(symbol = ticker, interval = interval, time_period = 60)
data.plot()
plt.title('BBands indicator for %s stock, at %s interval' % (ticker, interval))
plt.show()

# ------------------------------
# Part Three: Sector Performance
# ------------------------------

sp = SectorPerformances(key = 'API_KEY', output_format = 'pandas')
data, metadata = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind = 'bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()

# ---------------------------
# Part Four: Cryptocurrencies
# ---------------------------
ticker = 'BTC'
cc = CryptoCurrencies(key = 'YOUR_API_KEY', output_format = 'pandas')
data, metadata = cc.get_digital_currency_intraday(symbol = ticker, market = 'CNY')
data['1b. price (USD)'].plot()
plt.tight_layout()
plt.title('Intraday value for bitcoin (BTC)')
plt.grid()
plt.show()

# --------------------------------
# Part Five: Foreign Exchange (FX)
# --------------------------------
fe = ForeignExchange(key = 'YOUR_API_KEY')
# No metadata here
data, _ = fe.get_currency_exchange_rate(from_currency = 'BTC', to_currency = 'USD')
pprint(data)
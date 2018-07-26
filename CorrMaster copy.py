import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt

###Since Yahoo pulled their API the DataReader will not longer work. Can still work with a .csv###

#GFC Peak to trough#
start = dt.datetime(2007, 10, 9)
end = dt.datetime(2009, 3, 9)

#Custom dates#
##start = dt.datetime(2007, 1, 1)
##end = dt.datetime(2018, 2, 23)

#Sector Tickers#
tickers = ['XLV', 'XLU', 'XLE', 'XLB', 'XLI', 'XLP', 'XLRE', 'XLF', 'XLY', 'XLK', 'SPY']

#Defense Tickers
#tickers = ['BA', 'UTX', 'LMT', 'GD', 'RTN', 'COL', 'LLL', 'TDG', 'HII', 'SPR']

df = web.DataReader(tickers, 'yahoo', start, end)
df1 = web.DataReader('spy', 'yahoo', start, end)

#Extract closing price#
price = df['Close']
spx = df1['Close']

#Calculate daily percent change#
ret = price.pct_change()
spxret = spx.pct_change()

#Annual percent change#
pct = price.pct_change(periods=252, limit=200)*100
#print(pct.tail(5))

#Rolling correlation#
corr = ret.rolling(100, min_periods=50).corr(spxret)

#Daily correlation#
corr1 = ret.corr()

#Plot annual percent change#
##pct.plot()
##plt.title('Percent Change from Year Prior')
##plt.show()

#Plot  rolling correlation#
corr.plot()
plt.title('Rolling Correlation to SPY')
plt.show()

#Plot daily correlation#
corr1.plot()
plt.title('Basic Correlations')
plt.show()

x= ('corr1')
y= ('spxret')

#Scatter Plot#
plt.scatter(x, y, label='Correlation', color='k', marker='*')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Correlation')
plt.legend()
plt.show()




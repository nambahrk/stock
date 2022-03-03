#mpl_financeは非推奨
import mplfinance as mpf
from pandas_datareader import data
import matplotlib.pyplot as plt
import talib

#銘柄
number=7203

# 株価データを取得(stooqはデータ提供元)
def makeDataFrame(code):
  df_temp = data.DataReader("{}.JP".format(code), "stooq")
  df = df_temp.loc[:,['Open','High','Low','Close','Volume']].sort_values('Date')
  return df

#取得株、tailは最新データ取得数
df = makeDataFrame(number).tail(100)

open = df['Open']
high = df['High']
low = df['Low']
close = df['Close']
volume = df['Volume']

#RSI - Relative Strength Index
rsi9 = talib.RSI(close, timeperiod=9)
rsi14 = talib.RSI(close, timeperiod=14)

plt.plot(rsi9,label='rsi9')
plt.plot(rsi14,label='rsi14')
plt.xlabel('index')
plt.ylabel('indicator value')
plt.legend()
plt.show()
plt.savefig("rsi.png")

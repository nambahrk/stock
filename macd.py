#MACD=Moving Average Convergence Divergence
#MACD＝短期EMA-長期EMA(EMA：Exponential Moving Average)
#シグナル＝MACDの指数平滑移動平均線

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

#定義
open = df['Open']
high = df['High']
low = df['Low']
close = df['Close']
volume = df['Volume']

#MACD - Moving Average Convergence/Divergence(通常：短期12日、長期26日、シグナル9日)
macd, macdsignal, macdhist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

plt.plot(macd,label='macd')
plt.plot(macdsignal,label='macdsignal')
plt.bar(macdhist.index,macdhist ,label='macdhist')
plt.xlabel('index')
plt.ylabel('indicator value')
plt.legend()
plt.show()
plt.savefig("macd.png")

#mpl_financeは非推奨
import mplfinance as mpf
from pandas_datareader import data

#銘柄
number=7203

# 株価データを取得(stooqはデータ提供元)
def makeDataFrame(code):
  df_temp = data.DataReader("{}.JP".format(code), "stooq")
  df = df_temp.loc[:,['Open','High','Low','Close','Volume']].sort_values('Date')
  return df

#取得株、tailは最新データ取得数
df = makeDataFrame(number).tail(100)

#plot。lineはそのまま出力、candleはローソク足(defaultは推移線)、mavでx日平均線を描ける、df[]ではデータ数。
mpf.plot(df[:100],type='candle', mav=(5, 25, 75) , volume=True)
mpf.plot(df[:100],type='candle', mav=(5, 25, 75) , volume=True , title=str(number) , savefig=str(number) + ".png")

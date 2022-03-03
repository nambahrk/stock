from pandas_datareader import data
import mplfinance as mpf

start = '2021-04-01'
end = '2022-03-03'

df = data.DataReader('^N225','yahoo', start, end)

#plot。lineはそのまま出力、candleはローソク足(defaultは推移線),volumeで出来高表示
mpf.plot(df, type='candle', title="Nikkei stock average", volume=True )
mpf.plot(df, type='candle', title="Nikkei stock average" , volume=True , savefig="nikkei.png")

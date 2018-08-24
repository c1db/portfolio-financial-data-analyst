# portfolio-financial-data-analyst
This portfolio contains notebooks and scripts for monitoring, analyze and save stock data

fast_saver.py - is used for saving market snapshot once a minute in directory "fast_dump"  
fast_dump - this directory contains Bittrex snapshots

fast_analyze.ipynb - is used for sliding monitoring market state (first version) and market historical data
windows.ipynb - advanced version of fast_analyze.ipynb 

find_large_orders.py - is used for finding large orders on OKex BTC quarter futures
true_volume.ipynb - this notebook get trade data from Bitfinex and draw buy volume and sell volume

candellstick.ipynb - this notebook get latest trade data from single coin from Bittrex and draw 1 minute realtime candellstick

pump_view.ipynb - is used for finding abrupt change of price or volume on Bittrex(my first script)

analytical_combine.ipynb - is used for advansed analyse altcoins markets: processing of historical data, outliers finding, visualize price and volume data

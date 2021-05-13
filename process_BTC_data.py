import os, csv

timeint = {'1m': 60, '5m': 300, '10m': 600, '15m': 900, '30m': 1800, '1hr': 3600}
timeper = {'2017-bullrun': (1497672000,1513486800),'2017-bearrun': (1513486800,1529208000),
           '2019-flatdown': (1561521600,1577336400), '2019-flatup': (1588305600,1604203200)}



#print(timeper['2017-bullrun'][0])

def process_data(sym='BTCUSD',ti='15m',tp='2017-bullrun'):
    filename = '%s-%s-%s.csv' %(sym, ti, tp)
    if not os.path.isfile(filename):
      with open('bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv','r') as inp, open (filename,'w',newline='') as out:
         writer = csv.writer(out)
         for row in csv.reader(inp):
               i=int(row[0])
               beg = timeper[tp][0]
               end = timeper[tp][1]
               rem = (i-beg) % timeint[ti]

               if i >= beg and i <= end and rem == 0:
                  if row[1] != 'NaN':  # leave this alone
                     writer.writerow(row)

process_data('BTCUSD','15m')

""" def get_all_binance(symbol, kline_size, save = False):
    filename = '%s-%s-data.csv' % (symbol, kline_size)
    if os.path.isfile(filename): data_df = pd.read_csv(filename)
    else: data_df = pd.DataFrame()
    oldest_point, newest_point = minutes_of_new_data(symbol, kline_size, data_df, source = "binance")
    delta_min = (newest_point - oldest_point).total_seconds()/60
    available_data = math.ceil(delta_min/binsizes[kline_size])
    if oldest_point == datetime.strptime('1 Jan 2017', '%d %b %Y'): print('Downloading all available %s data for %s. Be patient..!' % (kline_size, symbol))
    else: print('Downloading %d minutes of new data available for %s, i.e. %d instances of %s data.' % (delta_min, symbol, available_data, kline_size))
    klines = binance_client.get_historical_klines(symbol, kline_size, oldest_point.strftime("%d %b %Y %H:%M:%S"), newest_point.strftime("%d %b %Y %H:%M:%S"))
    data = pd.DataFrame(klines, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
    if len(data_df) > 0:
        temp_df = pd.DataFrame(data)
        data_df = data_df.append(temp_df)
    else: data_df = data
    data_df.set_index('timestamp', inplace=True)
    if save: data_df.to_csv(filename)
    print('All caught up..!')
    return data_df """
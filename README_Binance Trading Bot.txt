BINANCE API CONNECTIVITY

https://www.youtube.com/watch?v=d-2GoqQbagI&list=PLvzuUVysUFOuB1kJQ3S2G-nB7_nHhD7Ay&index=2

https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
	Socket to retrieve live data from Binance
	wss://stream.binance.com:9443

1. Download and install node.js and VS Code
	run following commands in CMD to verify proper installation (will return version numbers)
	node -v
	npm -v
2. In CMD, run
	npm install -g wscat
	(you can type "wscat" to view available functions)
3. View trades for BTCUSDT
	wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade

4. View KLine (candlestick data)
	wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_15m

5. Save K Line data to file
	wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_15m | tee dataset.txt
	  (tee will pipe data to the console and a file)

6. Install python and pip
	Python from Windows store
	pip from get-pip.py file
		In CMD from folder with the file get-pip.py run 
			python get-pip.py

7. Install python-binance, run
	pip install python-binance

8. Install TA-Lib with Python wrapper (https://www.lfd.uci.edu/~gohlke/pythonlibs/  --> find TA-Lib)
	a) Type python into CMD to identify python version
	b) Dowload TA-Lib wrapper from website with correct version (3.9 --> cp39)
	c) Locate file in C:\Users\Username or C:\ and navigate to that folder in CMD
	d) Run pip install TA_Lib-0.4.19-cp39-cp39-win_amd64.whl
	e) Verify
		i) In VS Code terminal, type python
		ii) use import talib command (if no error, success)
		iii) type quit() to exit python

9. Install numpy
	run pip install numpy
		You can now test TA-Lib

10. Install backtrader and flask
	pip install backtrader
	pip install flask
	pip install matplotlib
	(if you get an error "cannot import name 'warnings' from 'matplotlib.dates' downgrade)
		pip uninstall matplotlib
		pip install matplotlib==3.2.2
	pip install pandas
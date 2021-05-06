from flask import Flask, request, render_template, jsonify, url_for, redirect

import os
import yfinance as yf


graphDest = os.path.join('static')


#-----------------------------------------------------Start of Utility Functions-----------------------------------------------------

#-----------------------------------------------------Save Results Plot-----------------------------------------------------
def saveplots(cerebro, numfigs=1, iplot=True, start=None, end=None,
			  width=16, height=9, dpi=300, tight=True, use=None, file_path='', **kwargs):
	from backtrader import plot
	if cerebro.p.oldsync:
		plotter = plot.Plot_OldSync(**kwargs)
	else:
		plotter = plot.Plot(**kwargs)

	figs = []

	for stratlist in cerebro.runstrats:

		for si, strat in enumerate(stratlist):
			rfig = plotter.plot(strat, figid=si * 100,
								numfigs=numfigs, iplot=iplot,
								start=start, end=end, use=use)
			figs.append(rfig)

	for fig in figs:
		for f in fig:
			f.savefig(file_path, bbox_inches='tight')
	return figs
#-----------------------------------------------------End of Utility Functions-----------------------------------------------------

#-----------------------------------------------------Instantiate Flask app--------------------------------------------------------
app = Flask(__name__)
app.debug = True

#-----------------------------------------------------Start Flask Routes-----------------------------------------------------------

# Route for testing strategies page
@app.route("/testing", methods = ['GET', 'POST'])
def backTesting():

	# Grabs Data from 01/01/2015 -> Today
	if request.method == 'POST':  # user has submitted a stock ticker
		symbol = request.args.get('searchbar', default="AAPL")
		tickerTag = yf.Ticker(symbol)
		tickerTag.actions.to_csv("data.csv")

		import strategy
		saveplots(strategy, file_path = os.path.join(graphDest, 'pnl.png'))
		starting_value = strategy.starting_portfolio_value
		ending_value = strategy.final_portfolio_value
		return redirect(url_for('graph',
								starting_value=int(starting_value),
								ending_value=int(ending_value)
								))# generate plot and description
	return render_template("backTest.html")
# Route for graphing page
@app.route('/graph/<starting_value>/<ending_value>', methods=['GET', 'POST'])
def graph(starting_value, ending_value):
	starting_value = int(starting_value)
	ending_value = int(ending_value)
	returns = ((ending_value - starting_value) / starting_value) * 100
	yearly_returns = returns / 4
	return render_template(
		"graph.html",
		pnl_chart=url_for('static', filename='pnl.png'),
		returns=str(returns),
		starting_value=str(starting_value),
		ending_value=str(ending_value),
		yearly_returns=yearly_returns)

# API Route for pulling the stock quote
@app.route("/quote", methods = ['GET', 'POST'])
def display_quote(symbol):
	# get a stock ticker symbol from the query string
	# default to AAPL
	symbol = request.args.get('symbol', default="AAPL")
	# pull the stock quote
	quote = yf.Ticker(symbol)


	#return the object via the HTTP Response
	return jsonify(quote.info)

# API route for pulling the stock history
@app.route("/history", methods = ['GET', 'POST'])
def display_history():
	#get the query string parameters
	symbol = request.args.get('symbol', default="AAPL")
	period = request.args.get('period', default="1y")
	interval = request.args.get('interval', default="1mo")

	#pull the quote
	quote = yf.Ticker(symbol)	
	#use the quote to pull the historical data from Yahoo finance
	hist = quote.history(period=period, interval=interval)
	#convert the historical data to JSON
	data = hist.to_json()

	#return the JSON in the HTTP response
	return data

@app.route("/")
def home():
	# we will use Flask's render_template method to render a website template.
    return render_template("homepage.html")
#-----------------------------------------------------End Flask Routes-----------------------------------------------------------


#-----------------------------------------------------Run Main App-----------------------------------------------------------
if __name__ == "__main__":
	app.run(debug=True)

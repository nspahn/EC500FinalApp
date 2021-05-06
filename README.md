# EC500FinalApp

## Abstract

This is a trading App based on python to run backtesting simulations and become a helpful trading tool. This tool is split into three main functions. BackTesting Trade Strategies, Displaying stock data, and set stock price alert. These functions are available through a GUI menu and allow navigation between the functions. The databases used throughout this application involve CSV files for simple local storage. The dependencies used for this program have been built into a requirments.txt file for simple instantiation. The APIs used throughout this project include:

1. yfinance
2. backtrader
3. NewsAPI
4. plotly
5. dash
6. stock-price-alerts

## *Timeline:*

- 4/14: User Stories, Functional Outline (Goal Met)
- 4/20: Skeleton Builds (Goal Met)
- 4/21: Unit Testing/Unit Functions (Finished 4/27)
- 5/1: Start Integration Testing (Working)
- 5/6: Polish App

### *5/5: Fix GitHub(Updating Problem) Dates dont reflect pushes in this repository*

## Step 1: Stub App

The Stub is the user stories and basic three functions outlined with how to accomplish them modularly. The initial Stub App involves

### *User Stories:*

- As a trader I want to backtest trading strategy parameters and understand how they would model future trades. I don’t want to run copious calculations and I want to compare backtests to see what gives me different buy, sell results.
- As a trader, strategy needs to be dynamic in that the tool should enable me to quickly identify multiple indicators that can indicate positive future opportunity.

### Functional Outline: *(Unit/Integration Testing)*

- BackTesting Function
  - Input Validation for Symbol - *UT*
  - Pull Symbol Data - *UT*
  - Run Simulation on Pulled Data - *IT*
  - Display Simulation Results - *IT*
- PrintCurrentData Function - *UT*
  - Input Validation for Symbol - *UT*
  - Pull Symbol Data - *UT*
  - Display Current Data - *IT*
- SetPriceAlert Function - *IT*
  - Input Validation for Symbol - *UT*
  - Pull Symbol Data - *UT*
  - Set HTTPSAlert Trigger - *UT*
  - Loop Pull StockData until Trigger - *UT*
  - Send Alert Email. - *UT*

## Update/Demo 1: (4-21-21)

At this point in development, much of the application's functionality has at least a skeleton build. The GUI leaves a lot to be desired. In the Stub, I outlined the basic functionality. Trying to build things out modularly prepares the unit tests' overall success before moving on to the integration testing. Currently, the idea is for the GUI to tie everything together with a file that can call all the functional components and save them to a database. SQL and CSV have different advantages, and the database choice will depend on where I can make the most progress on the GUI. I am currently using Tkinter to build a local experience, but I am having some issues with permissions and interacting in the database. Dash seems like an alternative that looks a lot better, and if I can implement it correctly, it provides a way to create this whole project utilizing a python framework to take care of the HTML/CSS and JS. Tkinter also has the issue that it needs to take in the current outputs from the Matlab plot, and it is not simple to integrate this visualization into an existing window. In favor of Tkinker is that Authentication is simple, and I know how to use it with a current database.

![tkinker GUI login](Documents/loginGUI.PNG "tkinker GUI login")
![plot figure](Documents/BTTestingFig.png "plot figure")
![back testing gif](Documents/BackTestingExample.gif "back testing gif")

## Update 2: (4-28-21)

At this point, I have decided I am going to go with Dash. I also learned how to do unit testing within Pycharm, which can run localized tests as I change things that will help test each function. The unit tests currently pass basic tests. I am looking to move on to integration testing next while integrating the dash GUI with updates from the database files. I am not sure if I will incorporate the Matlab plot results into the plot, but I will try to export the data used to build the Plotly visualization to get around this. I am having trouble integrating my local unit tests with the github workspac. I will try to get these tests working on github as well as locally. I am considering splitting up unit tests to my local machine and integration testing on githubn but both have advantages locally and withevery push so I am going to keep trying to do both.

![Dash Demo](Documents/Dash-Demo.png "Dash Page")

## Update 3: (5-1-21)

I have decided to do a little of both regarding the GUI. Matlab lib plot has the advantage of the plot over plotly in the backtesting area in that you can save the file and its nice to view the backtesting in a window in which it can be analysed and saved. The Plotly-dash GUI however works far better for graphically displaying current stock data. I still dont know how to integrate notifications menu but I may just leave it as a consol function given theres no visual element.

## Update 4: (5-3-21)

I wrote some code to translate a python 2 solution that was far too complicated. As it goes after some googling I found stock-price-alerts which I can use with a configuration file to send alerts. 

## Update 5: (5-5-21)
Finally, working on integration testing, I hope everything works well from here as it's not a lot that is being integrated. It's not as independent an app as I envisioned at the genesis of the design process, but it merged technical and practical teachings acquired from projects earlier in the semester.  I'm proud I could build something like this, which I would not have had the skill to do before this class. I will also take with me the process for modular development and building tests that reduced the timeline requirements of the project. 

## Update 6/Demo 2: (5-6-21)

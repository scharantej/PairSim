## Flask Application Design for Reinforcement Learning Pair Trading

### HTML Files

- **index.html:** Main landing page of the application, containing buttons or links to initiate the pair trading process and view the results.

- **results.html:** Displays the outcomes of the pair trading process, such as the trades executed, profit/loss, and other relevant statistics.

### Routes

- **@app.route('/')** (GET): Renders the index.html page.

- **@app.route('/trade')** (POST): Initiates the pair trading process. This route receives the necessary parameters (e.g., pairs to trade, time frame) and triggers the reinforcement learning algorithm for pair trading.

- **@app.route('/results')** (GET): Renders the results.html page, displaying the outcomes of the pair trading process.
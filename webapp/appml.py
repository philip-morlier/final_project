import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
with open(f'model/nfl_model_xgboost.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        posteam = flask.request.form['Possession Team']
        qtr = flask.request.form['Quarter']
        TOC = flask.request.form['Time on Clock']
        down = flask.request.form['Down']
        ydstogo = flask.request.form['Yards to Go']
        yrdln = flask.request.form['Yard Line']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[posteam, qtr, TOC, down, ydstogo, yrdln]],
                                       columns=['posteam', 'qtr', 'TOC', 'down', 'ydstogo', 'yrdln'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('index.html',
                                     original_input={'Possession Team':posteam,
                                                     'Down':down,
                                                     'Yard Line':yrdln},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()
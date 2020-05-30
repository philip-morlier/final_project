import flask
import pickle
import pandas as pd
import os
from transformation_methods import Transformer


with open(f'model/play_forest_v1.pkl', 'rb') as f:
    model = pickle.load(f)


app = flask.Flask(__name__, template_folder='templates')
@app.route('/')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        
   
        period = flask.request.form['quarter']
        quarter = Transformer().quarter_interpreter(period)
        clock_time = flask.request.form['time']
        play = flask.request.form['playtype']
        dn = flask.request.form['down']
        
        posteam = flask.request.form['posteam']
        ydstogo = flask.request.form['ydstogo']
        yardline_100 = flask.request.form['yardline'] 
        play_type_cat = Transformer().play_interpreter(play)
        down = Transformer().down_interpreter(dn)
        game_seconds_remaining = Transformer().time_converter(clock_time,quarter)
        ydsnet = flask.request.form['ydsnet']


        input_variables = pd.DataFrame([[posteam,ydstogo,yardline_100,play_type_cat,down,
                                game_seconds_remaining,ydsnet]],
                                columns=['posteam', 'ydstogo','yardline_100','play_type_cat','down',
                                        'game_seconds_remaining','ydsnet'])
        
        output = model.predict(input_variables)[0]

        prediction = Transformer().result_interpreter(output)


        return flask.render_template('main.html',
                                     result=prediction,
                                     )


if __name__ == '__main__':
    app.run()
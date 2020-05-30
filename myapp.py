import flask
import pickle
import pandas as pd
import os
from transformation_methods import *


with open(f'model/play_forest_v1.pkl', 'rb') as f:
    model = pickle.load(f)

post_data=Playdata()

# import pdb
# pdb.set_trace()

app = flask.Flask(__name__, template_folder='templates')
@app.route('/')


@app.route('/', methods=['GET', 'POST'])
def main():

    if flask.request.method == 'GET':


        play = flask.request.args.get('playtype','pass')
        play_type_cat = Transformer().play_interpreter(play)
        post_data.set_play_variable(play_type_cat)
        # post_play=post_data.get_variable()

        ydsnet = flask.request.args.get('ydsnet',5)
        post_data.set_yrd_variable(ydsnet)



        return(flask.render_template('pre_play.html'))



    if flask.request.method == 'POST':

        # pdb.set_trace()
        
   
        period = flask.request.form['quarter']
        quarter = Transformer().quarter_interpreter(period)
        clock_time = flask.request.form['time']
        dn = flask.request.form['down']
        
        posteam = flask.request.form['posteam']
        ydstogo = flask.request.form['ydstogo']
        yardline_100 = flask.request.form['yardline'] 
        play_type_cat = post_data.get_play_variable()
        down = Transformer().down_interpreter(dn)
        game_seconds_remaining = Transformer().time_converter(clock_time,quarter)
        ydsnet = post_data.get_yrd_variable()


        input_variables = pd.DataFrame([[posteam,ydstogo,yardline_100,play_type_cat,down,
                                game_seconds_remaining,ydsnet]],
                                columns=['posteam', 'ydstogo','yardline_100','play_type_cat','down',
                                        'game_seconds_remaining','ydsnet'])
        
        output = model.predict(input_variables)[0]

        prediction = Transformer().result_interpreter(output)


        return flask.render_template('main_2.html',result=prediction)


if __name__ == '__main__':
    app.run()
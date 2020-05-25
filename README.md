# final_project
Final project for the UO data bootcamp.

ETL Steps:

1. Create a Resources folder in the working tree
	- Save the Kaggle CSV data as 'NFL_play_by_play' in Resources folder (file size to large to post to GITHUB)
2. Open PG Admin on local machine
	- Create new DB titled, 'puntpasspredict'
3. Run Jupyter Notebook 'cleanedPlaybyPlat.ipynb'
	- This will drop unneed data, merge team_id and NFL_play_by_play into 1 dataframe. It will also export cleaned CSV file to Resources folder and load data into the PostgresDB





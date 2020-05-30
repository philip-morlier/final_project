-- Create a new table for TEAM ID
CREATE TABLE Team_ID (
  posteam VARCHAR(30) NOT NULL,
  team_id VARCHAR(30) NOT NULL
);

-- Create a new table for user_preplay_inputs
CREATE TABLE user_preplay_inputs (
  preplay_id SERIAL PRIMARY KEY,
  team_id VARCHAR(30) NOT NULL,
  qtr VARCHAR(30) NOT NULL,
  time_secs VARCHAR(30) NOT NULL,
  down VARCHAR(30) NOT NULL,
  ydstogo VARCHAR(30) NOT NULL,
  yrdln VARCHAR(30) NOT NULL
);

-- Create a new table for user_postplay_inputs
CREATE TABLE user_postplay_inputs (
  postplay_id SERIAL PRIMARY KEY,
  team_id VARCHAR(30) NOT NULL,
  play_type VARCHAR(30) NOT NULL,
  ydsnet VARCHAR(30) NOT NULL
);
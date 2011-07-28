-- create games table
DROP TABLE if EXISTS games;

CREATE TABLE games (
  id INTEGER NOT NULL PRIMARY KEY autoincrement,
  title VARCHAR(256) NOT NULL,
  owned BOOL NOT NULL,
  created TIMESTAMP NOT NULL,
  UNIQUE ("title")
);

-- create votes table
DROP TABLE if EXISTS votes;

CREATE TABLE votes (
  id INTEGER NOT NULL,
  game_id INTEGER NOT NULL REFERENCES "games" ("id"),
  created TIMESTAMP NOT NULL,
  PRIMARY KEY (id, game_id),
  UNIQUE ("game_id")
);

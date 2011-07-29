-- create games table
DROP TABLE if EXISTS votes_game;

CREATE TABLE "votes_game" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(256) NOT NULL UNIQUE,
    "owned" bool NOT NULL,
    "created" datetime NOT NULL
);

-- create votes table
DROP TABLE if EXISTS votes_vote;

CREATE TABLE "votes_vote" (
    "id" integer NOT NULL PRIMARY KEY,
    "game_id" integer NOT NULL REFERENCES "votes_game" ("id"),
    "count" integer unsigned NOT NULL,
    "created" datetime NOT NULL,
    UNIQUE ("id", "game_id")
);

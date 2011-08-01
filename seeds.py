#! /usr/bin/python
"""
this module is similar to RoR's seeds.
Use it to create test data.
>>> python seeds.py
"""
import sqlite3
import random
from datetime import datetime

DATABASE = 'nerds.sqlite'

# my favorite games
GAMES = (
    "Call of Duty: Black Ops", "Call of Duty: Modern Warfare 3", "Call of Duty: Modern Warfare 2", "Call of Duty: Modern Warfare",
    "Halo 4", "Halo 3", "Halo: Combat Evolved", "Halo Reach",
    "Medal of Honor", "Medal of Honor: Airborne", "Medal of Honor: Vanguard", "Medal of Honor: Frontline",
    "Madden NFL 11",
    "Avatar",
    "Portal 2",
    "Battlefield 3", "Battlefield: Bad Company",
    "Resident Evil 5", "Resident Evil: Operation Raccoon City",
    "Tomb Raider", "Tomb Raider: Underworld", "Tomb Raider: Legend",
    "Super Street Fighter IV",
    "Grand Theft Auto IV: Complete", "Grand Theft Auto: San Andreas",
    "Assassins Creed: Brotherhood", "Assassins Creed: II",
    "Fallout New Vegas",
    "LA Noire",
    "Mass Effect 2",
    "NBA 2K11",
    "Dead Space 2",
)

AMAZON_LINKS = {
    "Call of Duty: Black Ops": "http://www.amazon.com/Call-Duty-Black-Ops-Xbox-360/dp/B003JVKHEQ/ref=sr_1_1?ie=UTF8&qid=1312138847&sr=8-1",
    "Call of Duty: Modern Warfare 3": "http://www.amazon.com/Call-Duty-Modern-Warfare-Xbox-360/dp/B00503E8S2/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312138894&sr=1-1",
    "Call of Duty: Modern Warfare 2": "http://www.amazon.com/Call-Duty-Modern-Warfare-Xbox-360/dp/B00269QLI8/ref=sr_1_3?s=videogames&ie=UTF8&qid=1312138940&sr=1-3",
    "Call of Duty: Modern Warfare": "http://www.amazon.com/Call-Duty-Modern-Warfare-Xbox-360/dp/B0016B28Y8/ref=sr_1_4?s=videogames&ie=UTF8&qid=1312138968&sr=1-4",
    "Halo 4": "http://www.amazon.com/Halo-4-Xbox-360/dp/B0050SYX8W/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312139009&sr=1-1",
    "Halo 3": "http://www.amazon.com/Halo-3-Xbox-360/dp/B000FRU0NU/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312139048&sr=1-1",
    "Halo: Combat Evolved": "http://www.amazon.com/Halo-Combat-Evolved-Anniversary-Xbox-360/dp/B0050SYY5E/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312139081&sr=1-1",
    "Halo Reach": "http://www.amazon.com/Halo-Reach-Xbox-360/dp/B002BSA20M/ref=zg_bs_14220161_20",
    "Medal of Honor": "http://www.amazon.com/Medal-Honor-Xbox-360/dp/B000TI836G/ref=sr_1_2?s=videogames&ie=UTF8&qid=1312139269&sr=1-2",
    "Medal of Honor: Airborne": "http://www.amazon.com/Medal-Honor-Airborne-Xbox-360/dp/B000PE0HBS/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312139297&sr=1-1",
    "Medal of Honor: Vanguard": "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dvideogames&field-keywords=Medal+of+Honor%3A+Vanguard&x=11&y=12",
    "Medal of Honor: Frontline": "http://www.amazon.com/Medal-Honor-Frontline-Xbox/dp/B00006JC48/ref=sr_1_4?s=videogames&ie=UTF8&qid=1312139337&sr=1-4",
    "Madden NFL 11": "http://www.amazon.com/Madden-NFL-11-Xbox-360/dp/B002I0JB6E/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312139515&sr=1-1",
    "Avatar": "http://www.amazon.com/Avatar-Xbox-360/dp/B002EZOQVI/ref=sr_1_2?s=videogames&ie=UTF8&qid=1312139579&sr=1-2",
    "Portal 2": "http://www.amazon.com/Portal-2-Xbox-360/dp/B002I0J9M0/ref=sr_1_2?s=videogames&ie=UTF8&qid=1312139627&sr=1-2",
    "Battlefield 3": "http://www.amazon.com/Battlefield-3-Limited-Xbox-360/dp/B003O6G5TW/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312139922&sr=1-1",
    "Battlefield: Bad Company": "http://www.amazon.com/Battlefield-Bad-Company-Ultimate-Xbox-360/dp/B003VWGBC0/ref=sr_1_2?s=videogames&ie=UTF8&qid=1312139957&sr=1-2",
    "Resident Evil 5": "http://www.amazon.com/Resident-Evil-5-Xbox-360/dp/B000ZK6950/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312140009&sr=1-1",
    "Resident Evil: Operation Raccoon City": "http://www.amazon.com/Resident-Evil-Operation-Raccoon-Xbox-360/dp/B004UDLRMS/ref=sr_1_2?s=videogames&ie=UTF8&qid=1312140061&sr=1-2",
    "Tomb Raider": "http://www.amazon.com/Tomb-Raider-Xbox-360/dp/B004FSE52C/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312140109&sr=1-1",
    "Tomb Raider: Underworld": "http://www.amazon.com/Tomb-Raider-Underworld-Xbox-360/dp/B0012N8WXQ/ref=sr_1_2?s=videogames&ie=UTF8&qid=1312140123&sr=1-2",
    "Tomb Raider: Legend": "http://www.amazon.com/Tomb-Raider-Legend-Xbox-360/dp/B000A0XSN6/ref=sr_1_3?s=videogames&ie=UTF8&qid=1312140134&sr=1-3",
    "Super Street Fighter IV": "http://www.amazon.com/Super-Street-Fighter-IV-Xbox-360/dp/B002TDIEE0/ref=sr_1_2?s=videogames&ie=UTF8&qid=1312140154&sr=1-2",
    "Grand Theft Auto IV: Complete": "http://www.amazon.com/Grand-Theft-Auto-IV-Xbox-360/dp/B000FRU1UM/ref=sr_1_1?s=videogames&ie=UTF8&qid=1312140178&sr=1-1",
    "Grand Theft Auto: San Andreas": "http://www.amazon.com/Grand-Theft-Auto-San-Andreas-Xbox/dp/B000AX21VI/ref=sr_1_5?s=videogames&ie=UTF8&qid=1312140242&sr=1-5",
    "Assassins Creed: Brotherhood": "http://www.amazon.com/Assassins-Creed-Brotherhood-Xbox-360/dp/B003L8HQ7S/ref=zg_bs_14220161_31",
    "Assassins Creed: II": "http://www.amazon.com/Assassins-Creed-II-Xbox-360/dp/B00269DXCK/ref=zg_tr_14220271_29",
    "Fallout New Vegas": "http://www.amazon.com/Fallout-New-Vegas-Xbox-360/dp/B0028IBTL6/ref=zg_bs_14220161_33",
    "LA Noire": "http://www.amazon.com/L-Noire-Xbox-360/dp/B002I0HBZW/ref=zg_bs_14220161_34",
    "Mass Effect 2": "http://www.amazon.com/Mass-Effect-2-Xbox-360/dp/B001TORSII/ref=zg_tr_14220271_8",
    "NBA 2K11": "http://www.amazon.com/NBA-2K11-Xbox-360/dp/B003IMGC2C/ref=zg_tr_14220271_23",
    "Dead Space 2": "http://www.amazon.com/Dead-Space-2-Xbox-360/dp/B00309U0M6/ref=zg_tr_14220271_31",
}

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

# clear table before inserting new records
print "============================================="
print "Removing old records"
cur.execute("DELETE FROM votes_game")
cur.execute("DELETE FROM votes_vote")

print "============================================="
print "Creating game records"
# insert dummy video game inforamtion
for g in GAMES:
    cur.execute("""INSERT INTO votes_game ("title", "owned", "link", "created") VALUES (?, ?, ?, ?)""",
        (g, random.random() > 0.5, AMAZON_LINKS.get(g, ""), datetime.now()))

conn.commit()

print "============================================="
print "Creating vote records"
# insert vote records for games
cur.execute("SELECT * FROM votes_game")
rows = cur.fetchall()

for row in rows:
    cur.execute("""INSERT INTO votes_vote ("game_id", "count", "created") VALUES (?, ?, ?)""",
        (row[0], random.randint(10, 50) if row[2] else random.randint(1, 10), datetime.now()))

conn.commit()

cur.close()


print "============================================="
print "Dummy data have been successfully created!"
print "============================================="
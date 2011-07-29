import sqlite3
from datetime import datetime

DATABASE = 'nerds.sqlite'

# my favorite games
GAMES = (
    "Call of Duty: Black Ops", "Call of Duty: Modern Warfare 3", "Call of Duty: Modern Warfare 2", "Call of Duty: Modern Warfare 1",
    "Halo 4", "Halo 3", "Halo: Combat Evolved",
    "Medal of Honor", "Medal of Honor: Airborne", "Medal of Honor: Vanguard", "Medal of Honor: Frontline",
    "Madden NFL 11",
    "Uncharted 3: Drake's Deception", "Uncharted 2: Among Thieves", "Uncharted: Drake's Fortune",
    "Avatar",
    "Portal 2", "Portal",
    "inFAMOUS 2", "inFAMOUS",
    "God of War III", "God of War: Collection",
    "LittleBigPlanet",
    "Battlefield 3", "Battlefield: Bad Company", "Battlefield: Vietnam",
    "Resident Evil 5", "Resident Evil 4", "Resident Evil: Operation Raccoon City", "Resident Evil: The Darkside Chronicles",
    "Tomb Raider", "Tomb Raider: Underworld", "Tomb Raider: Legend",
    "Super Street Fighter IV",
    "Grand Theft Auto IV: Complete", "Grand Theft Auto: The Trilogy", "Grand Theft Auto: San Andreas", "Grand Theft Auto: Chinatown Wars",
)

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

# clear table before inserting new records
cur.execute("DELETE FROM votes_game")

# insert dummy video game inforamtion
for g in GAMES:
    cur.execute("""
        INSERT INTO votes_game ("title", "owned", "created") values (?, ?, ?)
    """, (g, False, datetime.now()))

conn.commit()
cur.close()

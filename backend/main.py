from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="LootHub API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


ITEMS = [
    {
        "id": "steam-warframe",

        "title": {
            "en": "Warframe",
            "tr": "Warframe",
            "es": "Warframe"
        },

        "description": {
            "en": "Free-to-play action game on Steam.",
            "tr": "Steam'de ücretsiz oynanabilen aksiyon oyunu.",
            "es": "Juego de acción gratuito en Steam."
        },

        "platform": "Steam",
        "type": "free",
        "category": "steam",
        "badge": "FREE",
        "icon": "⚔️",
        "theme": "purple",

        "tags": {
            "en": ["PC", "Action", "Steam"],
            "tr": ["PC", "Aksiyon", "Steam"],
            "es": ["PC", "Acción", "Steam"]
        },

        "sourceUrl":
            "https://store.steampowered.com/app/230410/Warframe/",

        "verified": True,

        "rewardType": None,
        "rewardAvailable": False
    }
]


@app.get("/")
async def home():

    return {
        "name": "LootHub API",
        "status": "online"
    }


@app.get("/api/drops")
async def get_drops():

    return {
        "items": ITEMS,
        "syncedAt": datetime.now(
            timezone.utc
        ).isoformat()
    }
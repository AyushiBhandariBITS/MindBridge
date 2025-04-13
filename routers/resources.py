from fastapi import APIRouter
import json
import os

router = APIRouter()

# Load and preprocess JSON data on startup
def load_hotlines_data():
    filepath = os.path.join("data", "hotlines.json")
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        country_map = {}
        for item in data["resources"]:
            country_name = item.get("country", "").strip().lower()
            country_map[country_name] = item
        return country_map

hotlines = load_hotlines_data()

@router.get("/{country}")
async def get_resources(country: str):
    normalized_country = country.strip().lower()
    resource = hotlines.get(normalized_country)

    if resource:
        return resource
    else:
        return {"message": f"No data available for '{country}'."}

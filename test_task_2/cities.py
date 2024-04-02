from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import sqlite3
from pydantic import BaseModel


app = FastAPI()
conn = sqlite3.connect('database.db')
# conn.row_factory = sqlite3.Row
# cursor = conn.cursor()


# cities = {
#     1:{
#         'name':'Moscow',
#         'latitude':55.751244,
#         'longitude':37.618423
#     },
#     2:{
#         'name':'Rome',
#         'latitude':41.89193,
#         'longitude':12.51133
#     },
#     3:{
#         'name':'Brooklyn',
#         'latitude':40.650002,
#         'longitude':-73.949997
#     },
#     4:{
#         'name':'Beijing',
#         'latitude':39.916668,
#         'longitude':-116.383331
#     },
#     5:{
#         'name':'Bishkek',
#         'latitude':42.882004,
#         'longitude':74.582748
#     }
# }
class cities(BaseModel):
    name: str
    latitude: float
    longitude: float

class UpdateCity(BaseModel):
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

@app.get('/')
def index():
    return {'info':'go to localhost/docs'}

@app.get('/get_city/{city_id}')
def get_city_by_id(city_id: int):
    return cities[city_id]
    # cursor.execute("SELECT * FROM cities WHERE id = ?", (city_id,))
    # city_row = cursor.fetchone()
    #
    # if city_row is None:
    #     # If city with given ID is not found, raise an HTTPException with 404 status
    #     raise HTTPException(status_code=404, detail="City not found")
    #
    # # Convert the database row to a dictionary and create a City object from it
    # city_data = dict(city_row)
    # return cities(**city_data)

@app.get('/get_city_by_name')
def get_city_by_name(name:str):
    for city in cities:
        if cities[city]['name']==name:
            return cities[city]
    return {'data':'not found'}

@app.post('/add_city/{city_id}')
def add_city(city_id:int, city:cities):
    if city_id in cities:
        return {'Error':'city exists'}

    cities[city_id] = city
    return cities[city_id]

@app.put('/update_city/{city_id}')
def update_city(city_id: int, city:UpdateCity):
    if city_id not in cities:
        return {'City':'not found'}

    if city.name != None:
        cities[city_id].name = city.name

    if city.latitude != None:
        cities[city_id].latitude = city.latitude

    if city.longitude != None:
        cities[city_id].longitude = city.longitude

    return cities[city_id]

@app.delete('/delete_city/{city_id}')
def delete_city(city_id:int):
    if city_id not in cities:
        return {'error':'city does not exist'}
    del cities[city_id]
    return {'message':'city deleted'}
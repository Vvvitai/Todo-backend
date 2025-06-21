import requests
from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    name: str
    mass: str
    gender: Optional[str]

def get_people():
    result = requests.get("https://swapi.tech/api/people/")
    return {'people' : [man['name'] for man in result.json()['results']]}


def get_person(person_id: str) -> dict:
    result = requests.get(f"https://swapi.tech/api/people/{person_id}/")
    name = result.json()['result']['properties']['name']
    gender = result.json()['result']['properties']['gender']
    mass = result.json()['result']['properties']['mass']
    person = Person(name=name, mass=mass, gender=gender)
    return person.model_dump()


print(get_person('1'))

from aloe import *
from aloe import tools
import requests
import json
from .. import config,logger
####First Scenario##############
@step('Adding cities with data')
def add_cities(self):
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/cities", json=row)
        results.append(res.status_code)
    world.cities = results
    logger.info(world.cities)

@step(r'Status code must be (\d+)')
def check_result_add(_, status_code):
    result = True
    for item in world.cities:
        result = result and item == int(status_code)
    assert result

####Secoend Scenario##############
@step('Add cities with data')
def add_cities(self):
    res = requests.post(f"{config.base_api_uri}/cities", json=tools.guess_types(self.hashes)[0])
    world.added = res.status_code

@step(r'Failure code must be (\d+)')
def check_unsuc_result(_, status_code):
    assert world.added == int(status_code)

####Third Scenario##################
@step('cities with data')
def add_cities(self):
    res = requests.post(f"{config.base_api_uri}/cities", json=tools.guess_types(self.hashes)[0])
    world.post = res.json()


@step(r'Cities row with slug (\S+) must be')
def check_city_added(self, slug: str):
    rows = tools.guess_types(self.hashes)
    logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/cities/{slug}", headers={"Accept-Language":"en-US"})
    logger.info(res.json())
    result2 = res.json()
    logger.info(result2)
    assert all((rows[0][key] == result2[key] for key in rows[0]))

####4th Scenario##############
# @step(r'the city rows must be unique in (\S+) field')
# def check_unique_slug(self, slug):
#     res= list()
#     res = requests.get(f"{config.base_api_uri}/cities/{slug}")


####5th Scenario##############
@step(r'Getting the list of cities')
def get_city_list(_):
    res = requests.get(f"{config.base_api_uri}/cities")
    logger.info(res.text)
    world.result = res.json()
    world.status = res.status_code


@step(r"Result code must be (\d+)")
def check_result(_, status_code):
    logger.info(world.status)
    assert world.status == int(status_code)


@step('List must not be empty')
def check_cities_list(_):
    assert len(world.result) > 0






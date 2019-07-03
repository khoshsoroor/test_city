from aloe import *
from aloe import tools
import requests
import json
from .. import config, logger
from ..cities import call

@before.each_feature
def delete_all_rows(_):
    call.deleteInBulk()


# ..... 1 Scenario ....#
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


@step(r'Cities row with slug (\S+) must be')
def check_city_added(self, slug: str):
    rows = tools.guess_types(self.hashes)
    res = requests.get(f"{config.base_api_uri}/cities/{slug}", headers={"Accept-Language": "en-US"})
    logger.info('get city response %s', res.text)
    result2 = res.json()
    assert all((rows[0][key] == result2[key] for key in rows[0]))


# ................2 Scenario...................#
@step(r'modify city row with slug (\S+)')
def successfully_modify_city(self, slug: str):
    res = requests.put(f"{config.base_api_uri}/cities/{slug}", json=tools.guess_types(self.hashes)[0])
    world.modify = res.status_code


@step(r'Modified code must be (\d+)')
def check_code_modified(_, status_code):
    logger.info(world.modify)
    assert world.modify == int(status_code)


@step(r'Modified cities row with slug (\S+) must be')
def checklist_city_modified(self, slug: str):
    rows = tools.guess_types(self.hashes)
    logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/cities/{slug}", headers={"Accept-Language":"en-US"})
    logger.info(res.json())
    result2 = res.json()
    logger.info(result2)
    assert all((rows[0][key] == result2[key] for key in rows[0]))


#.........3 Scenario..........................#
@step('Add cities with data')
def add_cities(self):
    res = requests.post(f"{config.base_api_uri}/cities", json=tools.guess_types(self.hashes)[0])
    world.added = res.status_code


@step(r'Failure code must be (\d+)')
def check_unsuc_result(_, status_code):
    assert world.added == int(status_code)


# ###4 Scenario############# #
@step(r'Getting the list of cities')
def get_city_list(_):
    res = requests.get(f"{config.base_api_uri}/cities")
    logger.info(res.text)
    world.city_list = res.json()
    logger.info("city list json", world.city_list)
    world.city_list_status = res.status_code


@step(r"Result code must be (\d+)")
def check_result_list(_, status_code):
    logger.info(world.city_list_status)
    assert world.city_list_status == int(status_code)


@step('List must not be empty')
def check_cities_list(_):
    assert len(world.city_list) > 0


####5 Scenario##############
@step(r'Delete city row with slug (\S+)')
def successfully_deleted_city(self, slug: str):
    res = requests.delete(f"{config.base_api_uri}/cities/{slug}")
    logger.info(res.status_code)
    world.deleted = res.status_code


@step(r'Successfully disabled code must be (\d+)')
def check_success_code_deleted(_, status_code):
    logger.info(world.deleted)
    assert world.deleted == int(status_code)


# ##########6 Scenario############# #
@step('Add cities with same slug')
def chk_unique(self):
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/cities", json=row)
        results.append(res.status_code)
    world.unique = results
    logger.info(world.unique)


@step(r'code should be (\d+)')
def check_result_unique(_, status_code):
    result = True
    for item in world.unique:
        result = result and item == int(status_code)
    assert result


#########7th Scenario##############
@step(r'Delete city row with wrong slug (\S+)')
def delete_wrong_city(self, slug : str):
    res = requests.delete(f"{config.base_api_uri}/cities/{slug}")
    world.wrong = res.status_code


@step(r'wrong slug for disable code must be (\d+)')
def check_success_code_deleted(_, status_code):
    logger.info(world.wrong)
    assert world.wrong == int(status_code)
from aloe import *
from aloe import tools
import requests
from .. import config, logger

# # ...............................1................................. #
# @step('Getting the list of services')
# def get_services_list(_):
#     res = requests.get(f"{config.base_api_uri}/services")
#     logger.info(res.text)
#     world.services_list = res.json()
#     logger.info(world.services_list)
#     world.services_status = res.status_code
#
#
# @step(r"Result code must be (\d+)")
# def check_result_code_list(_, status_code):
#     logger.info(world.services_status)
#     assert world.services_status == int(status_code)
#
#
# #..............2..........................#
# @step(r'Getting the list of services by slug (\S+)')
# def get_service_detail(self, slug: str):
#     res = requests.get(f"{config.base_api_uri}/services/{slug}")
#     logger.info(res.text)
#     world.service_detail = res.json()
#     logger.info(world.service_detail)
#     world.service_detail_status = res.status_code
#
#
# @step(r"status code is (\d+)")
# def check_result_code_list(_, status_code):
#     logger.info(world.service_detail_status)
#     assert world.service_detail_status == int(status_code)
#
#
# #................3.........................#
# @step('Register an service with data:')
# def add_service(self):
#     results = list()
#     for row in tools.guess_types(self.hashes):
#         res = requests.post(f"{config.base_api_uri}/services", json=row)
#         results.append(res.status_code)
#     world.services = results
#     logger.info(world.services)
#
#
# @step(r'Successfully register code must be (\d+)')
# def chk_result_add_services(_, status_code):
#     result = True
#     for item in world.services:
#         result = result and item == int(status_code)
#     assert result
#
#
# @step(r'Service detail with slug (\S+) must be')
# def chk_services_added(self, slug: str):
#     rows = tools.guess_types(self.hashes)
#     logger.info(rows)
#     res = requests.get(f"{config.base_api_uri}/services/{slug}", headers={"Accept-Language": "en-US"})
#     logger.info(res.json())
#     result2 = res.json()
#     logger.info(result2)
#     assert all((rows[0][key] == result2[key] for key in rows[0]))


# ...................4........................ #
# @step('add service with invalid data')
# def add_cities(self):
#     res = requests.post(f"{config.base_api_uri}/services", json=tools.guess_types(self.hashes)[0])
#     world.empty = res.status_code
#
#
# @step(r'status code for invalid data must be (\d+)')
# def chk_invalid_result(_, status_code):
#     assert world.empty == int(status_code)
#
#
# # ...................5........................ #
# @step(r'modify service row with slug (\S+)')
# def success_modify_services(self, slug: str):
#     res = requests.put(f"{config.base_api_uri}/services/{slug}", json=tools.guess_types(self.hashes)[0])
#     world.su_modify = res.status_code
#
#
# @step(r'Modify code must be (\d+)')
# def chk_code_su_modified(_, status_code):
#     logger.info(world.su_modify)
#     assert world.su_modify == int(status_code)
#
#
# @step(r'Modified services row with slug (\S+) must be')
# def chk_services_modified(self, slug: str):
#     rows = tools.guess_types(self.hashes)
#     logger.info(rows)
#     res = requests.get(f"{config.base_api_uri}/cities/{slug}", headers={"Accept-Language":"en-US"})
#     logger.info(res.json())
#     result2 = res.json()
#     logger.info(result2)
#     assert all((rows[0][key] == result2[key] for key in rows[0]))
#
#
# # .....................6 ...................#
# @step(r'Delete service row with slug (\S+)')
# def successfully_deleted_service(self, slug: str):
#     res = requests.delete(f"{config.base_api_uri}/services/{slug}")
#     logger.info(res.status_code)
#     world.service_deleted = res.status_code
#
#
# @step(r'Successfully disabled code for service must be (\d+)')
# def chk_service_code_deleted(_, status_code):
#     logger.info(world.service_deleted)
#     assert world.service_deleted == int(status_code)
#
#
# # ...................7....................#
# @step('Add services with same slug')
# def chk_unique_service(self):
#     results = list()
#     for row in tools.guess_types(self.hashes):
#         res = requests.post(f"{config.base_api_uri}/services", json=row)
#         results.append(res.status_code)
#     world.uni_service = results
#     logger.info(world.uni_service)
#
#
# @step(r'services unique code should be (\d+)')
# def check_result_uni_(_, status_code):
#     result = True
#     for item in world.unique:
#         result = result and item == int(status_code)
#     assert result

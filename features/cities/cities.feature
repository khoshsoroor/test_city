Feature: City list query check and add city
  Check if city list query works
  and add city

#..................1................#
#  Scenario: successful add cities
#    When Adding cities with data
#      | slug   | title|  is_active |
#      | tehran | تهران|  false     |
#      | karaj  | کرج  |  true      |
#    Then Status code must be 201

#..................2................#
#    Scenario: Unsuccessful add cities
#    When Add cities with data
#      | slug   | title|  is_active |
#      | tehran | تهران|       |
#    Then Failure code must be 400

#..................3................#
#  Scenario: Check cities correctly added
#    When  cities with data
#      | slug   | title|  is_active |
#      | tehran | تهران|  true      |
#    Then Cities row with slug tehran must be
#      | slug   | title| is_active |
#      | tehran | تهران|  true     |

#..................4................#
#  Scenario: Check Unique in slug field
#    When Add cities with same slug
#       | slug   | title|  is_active |
#       | tehran | تهران|  true      |
#       | tehran | تهران|  true      |
#    And Get cities list
#    Then code should be 400

#..................5................#
#  Scenario: Getting City list
#    When Getting the list of cities
#    Then Result code must be 200
#    And List must not be empty


#  Scenario: Delete some rows in cities
#    When Delete city row with slug tehran
#    Then
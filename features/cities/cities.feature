Feature:Test City C,R,U,D

..................1................#
  Scenario: successful add cities
    When Adding cities with data
      | slug   | title|  is_enabled|
      | tehran | تهران|  true     |
      | karaj  | کرج  |  true     |
    Then Status code must be 201
    And Cities row with slug tehran must be
      | slug   | title| is_enabled |
      | tehran | تهران|  true     |

#..................2 ..................#
  Scenario: Successfully modified the city
    When modify city row with slug tehran
      | slug   | title | is_enabled |
      | tehran | مهسا  |  true     |
    Then Modified code must be 204
    And Modified cities row with slug tehran must be
      | slug   | title| is_enabled |
      | tehran |  مهسا|  true     |

#..................3................#
    Scenario: Unsuccessful add cities
    When Add cities with data
      | slug   | title|  is_enabled|
      | tehran | تهران|       |
    Then Failure code must be 400

#..................4................#
  Scenario: Getting City list
    When Getting the list of cities
    Then Result code must be 200
    And List must not be empty

#..................5...............#
  Scenario: Successfully Delete row in cities
    When Delete city row with slug tehran
    Then Successfully disabled code must be 204


#..................6................#
  Scenario: Check Unique in slug field
    When Add cities with same slug
       | slug   | title|  is_enabled |
       | tehran2 | تهران|  true      |
       | tehran2 | تهران|  true      |
    Then code should be 400

#..................7................#
  Scenario: Delete wrong row in cities
    When Delete city row with wrong slug n
    Then wrong slug for disable code must be 404



Feature:Test services C,R,U,D


##......................3............................#
#    Scenario: Successful Register new service
#        When Register a service with data:
#            | slug           | title      | is_active |
#            | nezafat-manzel | نطافت منزل |  true     |
#        Then Successfully register code must be 201
#        And  Service detail with slug nezafat-manzel must be
#             | slug           | title      | is_active |
#             | nezafat-manzel | نطافت منزل |  true     |
#
##..................1....................#
#    Scenario: Getting Services list
#        When Getting the list of services
#        Then Result code must be 200
#
##..................2....................#
#    Scenario: show Service details from specific slug
#        When Getting the list of services by slug nezafat-manzel
#        Then status code is 200


#........................4..................................#
#    Scenario: Unsuccessful Register services with empty data
#        When add service with invalid data
#             | slug           | title      | is_active |
#             | nezafat-manzel |            |  true     |
#        Then status code for invalid data must be 400
#
#
##........................5..................................#
#    Scenario: Successfully modified the services
#        When modify service row with slug nezafat-manzel
#             | slug           | title | is_active |
#             | nezafat-manzel | مهسا  |  true     |
#        Then Modify code must be 204
#        And Modified services row with slug tehran must be
#             | slug   | title | is_active |
#             | tehran |  مهسا |  true     |
#
##.....................6.............................................#
#   Scenario: Successfully Delete row in services
#       When Delete service row with slug nezafat-manzel
#       Then Successfully disabled code for service must be 204
#
#
##..................7......................................................#
#   Scenario: Check Unique in slug field
#       When Add services with same slug
#           | slug   | title|  is_active |
#           | tehran | تهران|  true      |
#           | tehran | تهران|  true      |
#       Then services unique code should be 400

##..............................#
#  Scenario: Delete wrong row in cities
#    When Delete city row with wrong slug n
#    Then wrong slug for disable code must be 404

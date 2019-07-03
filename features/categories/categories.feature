Feature:Test Categories C,R,U,D


 # ......................1............................#
    Scenario: Successful Register new categories
        When Register a category with data:
            | slug           | title      | is_enabled |
            | nezafat-manzel | نطافت منزل |  true     |
        Then Successfully categoris code must be 201
        And  Service detail with slug nezafat-manzel must be
             | slug           | title      | is_active |
             | nezafat-manzel | نطافت منزل |  true     |
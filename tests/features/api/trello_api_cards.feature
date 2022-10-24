@api @trello_cards
Feature: Cards Manager for Trello API
  As an application developer,
  I want to manage trello cards via a REST API,
  So that my app can get answers and show them.

  @fixture_create_cards @api @fixture_delete_organizations @trello_cards
  Scenario: Get a Card
    When a "GET" request to "/cards/<cards.id>" is send
    Then the response status code should be "200"
    And the response schema should be verified with "get_card_schema.json"

  @fixture_create_cards @api @fixture_delete_organizations @trello_cards
  Scenario: Get the board of a card
    When a "GET" request to "/cards/<cards.id>/board" is send
    Then the response status code should be "200"
  
  @fixture_create_cards @api @fixture_delete_organizations @trello_cards
  Scenario: Get the list of a card
    When a "GET" request to "/cards/<cards.id>/list" is send
    Then the response status code should be "200"
 
  @fixture_create_lists @api @fixture_delete_organizations @trello_cards
  Scenario: Create a Card
    Given the following body parameters:
      | key         | value            |
      | name        | CREATE_CARD_NAME |
      | idList      | <lists.id>       |
      | pos         | top              |
      | desc        | MY_DESC          |
    When a "POST" request to "/cards" is send
    Then the response status code should be "200"
    And the body of the "card" should contain:
      | key         | value            |
      | name        | CREATE_CARD_NAME |
      | idList      | <lists.id>       |
      | pos         | top              |
      | desc        | MY_DESC          |
    And the response schema should be verified with "create_card_schema.json"

  @fixture_create_cards @api @fixture_delete_organizations @trello_cards
  Scenario: Delete a Card
    When a "DELETE" request to "/cards/<cards.id>" is send
    Then the response status code should be "200"
    And the response schema should be verified with "delete_card_schema.json"

  @fixture_create_cards @api @fixture_delete_organizations @trello_cards
  Scenario: Update a Card
    Given the following body parameters:
      | key         | value           |
      | name        | UPDATED_NAME    |
      | pos         | bottom          |
      | desc        | UPDATED_DESC    |
    When a "PUT" request to "/cards/<cards.id>" is send
    Then the response status code should be "200"
    And the "name" of the "card" should be "UPDATED_NAME" 
    And the body of the "card" should contain:
      | key         | value            |
      | name        | UPDATED_NAME     |
      | pos         | bottom           |
      | desc        | UPDATED_DESC     |
    And the response schema should be verified with "update_card_schema.json"

  @fixture_create_lists @api @fixture_delete_organizations @negative_test @trello_cards
  Scenario: Create a Card with an wrong List ID
    Given the following body parameters:
      | key         | value                     |
      | name        | CREATE_CARD_NAME          |
      | idList      | 6352b6132086d8002af78f9e  |
    When a "POST" request to "/cards" is send
    Then the response status code should be "404"

  @fixture_create_cards @api @fixture_delete_organizations @negative_test @trello_cards
  Scenario: Delete a Card with an wrong ID
    When a "DELETE" request to "/cards/634ecbfd01161f0490435f78" is send
    Then the response status code should be "404"

  @fixture_create_cards @api @fixture_delete_organizations @negative_test @trello_cards
  Scenario: Update a Card with an wrong ID
    Given the following body parameters:
      | key         | value           |
      | name        | UPDATED_NAME    |
    When a "PUT" request to "/cards/634ecbfd01161f0490435f78" is send
    Then the response status code should be "404"

  @fixture_create_cards @api @fixture_delete_organizations @negative_test @trello_cards
  Scenario: Get a Card with an invalid ID
    When a "GET" request to "/cards/1234567890" is send
    Then the response status code should be "400"

  @fixture_create_cards @api @fixture_delete_organizations @negative_test @trello_cards
  Scenario: Get a Card with an wrong ID
    When a "GET" request to "/cards/634ecbfd01161f0490435f78" is send
    Then the response status code should be "404"

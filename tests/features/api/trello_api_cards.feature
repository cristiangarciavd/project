@api @trellocards
Feature: Cards Manager for Trello API
  As an application developer,
  I want to manage trello cards via a REST API,
  So that my app can get answers and show them.

  @fixture_delete_lists @fixture_create_cards @fixture_delete_cards @fixture_create_boards @fixture_delete_boards @fixture_create_lists @api @fixture_create_organizations @fixture_delete_organizations
  Scenario: Get a Card
    Given a "GET" request to Trello API cards is queried with "<card_id>"
    Then the response status code should be "200"
    # Examples:
    #   | card_id                   | status_code |
    #   | 634ecbfd01161f0490435f72  | 200         |
    #   | 634ecbfd01161f0490435f77  | 404         |
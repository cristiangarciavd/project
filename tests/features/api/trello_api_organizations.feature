@api @trello_organizations
Feature: Cards Manager for Trello API
  As an application developer,
  I want to manage trello cards via a REST API,
  So that my app can get answers and show them.

@fixture_delete_only_organization @api @trello_organizations
  Scenario: Create a Organization
    Given the following body parameters:
      | key         | value            |
      | displayName | CREATE_ORG_NAME  |
      | name        | ORG_NAME         |
      | desc        | MY_DESC          |
    When a "POST" request to "/organizations" is send
    Then the response status code should be "200"
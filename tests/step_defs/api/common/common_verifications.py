"""
This module contains step definitions for trello api actions.
"""
from pytest_bdd import then, parsers
from main.trello.api.trello_cards import TrelloCard

@then(parsers.parse('the response status code should be "{status_code}"'))
def trelo_card_response_code(trelo_card_response, status_code):
    assert str(trelo_card_response[1]) == status_code
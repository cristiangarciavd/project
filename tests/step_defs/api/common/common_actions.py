"""
This module contains step definitions for trello api actions.
"""
from pytest_bdd import given, parsers
from main.trello.api.trello_cards import TrelloCard

@given(parsers.parse('a "{http_method}" request to Trello API cards is queried with "{card_id}"'), 
       target_fixture="trelo_card_response")
def trelo_card_response(http_method, request):
    """Do request to the endpoint

    Args:
        http_method (string): http method or verb
        endpoint (string): endpoint used to interact with request manager
        request (request): request fixture object
    """
    return TrelloCard.get_card(request.context["cards"]["id"]) 

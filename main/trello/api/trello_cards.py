"""Provides a TrelloCard class to manage cards in Trello"""
from main.core.api.http_methods import HttpMethods
from main.trello.api.trello_routes import TrelloApiRoutes
from main.core.api.request_manager import RequestManager


class TrelloCard:
    """Trello cards requests
    """

    @staticmethod
    def create_card(list_id, **Kwargs):
        """Method to create new cards

        Args:
            list_id (str): list ID
        """
        endpoint_card = TrelloApiRoutes.CARDS.value
        return RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            endpoint_card,
            idList=list_id, 
            **Kwargs
        )

    @staticmethod
    def get_card(card_id, **Kwargs):
        """Method to get a card information

        Args:
            card_id (str): card ID
        """
        endpoint_card = f"{TrelloApiRoutes.CARDS.value}{card_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_card,
            **Kwargs
        )

    @staticmethod
    def update_card(card_id, **Kwargs):
        """Method to update a card information

        Args:
            card_id (str): card ID
        """
        endpoint_card = f"{TrelloApiRoutes.CARDS.value}{card_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.PUT.value,
            endpoint_card,
            **Kwargs
        )

    @staticmethod
    def delete_card(card_id):
        """Method to delete a card

        Args:
            card_id (str): card ID
        """
        endpoint_card = f"{TrelloApiRoutes.CARDS.value}{card_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.DELETE.value,
            endpoint_card
        )

    @staticmethod
    def get_cards_board(card_id, fields="all"):
        """Method to get the board the card is on

        Args:
            card_id (str): card ID
            fields (str): all or a comma-separated list of fields
        """
        endpoint_card = (TrelloApiRoutes.CARD_IN_BOARD.value).format(card_id)
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_card,
            fields=fields
        )

    @staticmethod
    def get_cards_list(card_id, fields="all"):
        """Method to get the list the card is on

        Args:
            card_id (str): card ID
            fields (str): all or a comma-separated list of fields
        """
        endpoint_card = (TrelloApiRoutes.CARD_IN_LIST.value).format(card_id)
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_card,
            fields=fields
        )

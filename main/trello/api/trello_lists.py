"""Provides a TrelloList class to manage lists in Trello"""
from main.core.api.http_methods import HttpMethods
from main.trello.api.trello_routes import TrelloApiRoutes
from main.core.api.request_manager import RequestManager


class TrelloList:
    """Trello lists requests
    """
    @staticmethod
    def get_all_list(board_id="", **Kwargs):
        """Get all list in the board

        Args:
            board_id (str, optional): board ID. Defaults to "".

        Returns:
            _type_: _description_
        """
        endpoint_lists = (TrelloApiRoutes.LIST_IN_BOARD.value).format(board_id)
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_lists,
            **Kwargs
        )

    @staticmethod
    def create_list(board_id, name, **Kwargs):
        """Create a list

        Args:
            board_id (str): board ID
            name (str): list name

        Returns:
            _type_: _description_
        """
        endpoint_list = (TrelloApiRoutes.LIST_IN_BOARD.value).format(board_id)
        return RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            endpoint_list,
            name=name,
            **Kwargs
        )

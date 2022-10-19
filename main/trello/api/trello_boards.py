"""Provides a TrelloBoard class to manage boards in Trello"""
from main.core.api.http_methods import HttpMethods
from main.trello.api.trello_routes import TrelloApiRoutes
from main.core.api.request_manager import RequestManager


class TrelloBoard:
    """Trello boards requests
    """

    @staticmethod
    def get_all_boards(**Kwargs):
        """Get all boards of the user
        """
        endpoint_board = TrelloApiRoutes.BOARDS.value
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_board,
            **Kwargs
        )

    @staticmethod
    def get_board(board_id="", **Kwargs):
        """Get a specific board with ID

        Args:
            board_id (str, optional): board ID. Defaults to "".
        """
        endpoint_board = f"{TrelloApiRoutes.BOARD.value}{board_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_board,
            **Kwargs
        )

    @staticmethod
    def create_board(name, **Kwargs):
        """Create a board

        Args:
            name (str): board name
        """
        endpoint_board = TrelloApiRoutes.BOARD.value
        return RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            endpoint_board,
            name=name,
            ** Kwargs
        )

    @staticmethod
    def update_board(board_id, **Kwargs):
        """Update a specific board with ID

        Args:
            board_id (str): board ID
        """
        endpoint_board = f"{TrelloApiRoutes.BOARD.value}{board_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.PUT.value,
            endpoint_board,
            **Kwargs
        )

    @staticmethod
    def delete_board(board_id):
        """Delete a specific board with ID

        Args:
            board_id (str): board ID
        """
        endpoint_board = f"{TrelloApiRoutes.BOARD.value}{board_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.DELETE.value,
            endpoint_board,
        )

from main.core.api.http_methods import HttpMethods
from main.trello.api.trello_routes import TrelloApiRoutes
from main.core.api.request_manager import RequestManager


class TrelloBoard:
    """Trello boards requests
    """

    @staticmethod
    def get_all_boards(**Kwargs):
        endpoint_board = TrelloApiRoutes.BOARDS.value
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_board,
            **Kwargs
        )
    @staticmethod
    def get_board(id="", **Kwargs):
        endpoint_board = f"{TrelloApiRoutes.BOARD.value}{id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_board,
            **Kwargs
        )
    @staticmethod
    def create_board(name,**Kwargs):
        endpoint_board = TrelloApiRoutes.BOARD.value
        return RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            endpoint_board,
            name=name,
            ** Kwargs
        )

    @staticmethod
    def update_board(id, **Kwargs):
        endpoint_board = f"{TrelloApiRoutes.BOARD.value}{id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.PUT.value,
            endpoint_board,
            **Kwargs
        )

    @staticmethod
    def delete_board(id):
        endpoint_board = f"{TrelloApiRoutes.BOARD.value}{id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.DELETE.value,
            endpoint_board,
        )
    

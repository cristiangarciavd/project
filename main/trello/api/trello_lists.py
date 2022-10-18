from main.core.api.http_methods import HttpMethods
from main.trello.api.trello_routes import TrelloApiRoutes
from main.core.api.request_manager import RequestManager


class TrelloList:
    """Trello lists requests
    """
    @staticmethod
    def get_all_list(id="", **Kwargs):
        endpoint_board = f"{TrelloApiRoutes.BOARD.value}{id}{TrelloApiRoutes.LIST.value}"
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_board,
            **Kwargs
        )
    @staticmethod
    def create_list(id, name,**Kwargs):
        endpoint_board = f"{TrelloApiRoutes.BOARD.value}{id}{TrelloApiRoutes.LIST.value}"
        return RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            endpoint_board,
            name=name,
            ** Kwargs
        )
    @staticmethod
    def manage_list(method, id="", **kwargs):
        """Manage List

        Args:
            id (str): list id
            method (str): get, update, delete, create
        """
        return RequestManager.get_instance().make_request(http_method=method, endpoint=f"/lists/{id}", **kwargs)
    
    @staticmethod
    def get_all_cards_on_list(id="", **kwargs):
        """Get all cads on the list

        Args:
            id (str): list id
        """
        return RequestManager.get_instance().make_request(http_method="get", endpoint=f"/lists/{id}/cards", **kwargs)

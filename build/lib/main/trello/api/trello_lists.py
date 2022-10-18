from main.core.api.request_manager import RequestManager

class TrelloList:
    """Trello lists requests
    """

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
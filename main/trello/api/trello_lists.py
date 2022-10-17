import sys
 
# setting path
sys.path.append('D:/JS/Api Testing/project')
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
        instance = RequestManager()
        return instance.make_request(http_method=method, endpoint=f"/lists/{id}", **kwargs)
    
    @staticmethod
    def get_all_cards_on_list(id="", **kwargs):
        """Get all cads on the list

        Args:
            id (str): list id
        """
        instance = RequestManager()
        return instance.make_request(http_method="get", endpoint=f"/lists/{id}/cards", **kwargs)
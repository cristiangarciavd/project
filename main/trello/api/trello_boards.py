import sys
 
# setting path
sys.path.append('D:/JS/Api Testing/project')
from main.core.api.request_manager import RequestManager

class TrelloBoard:
    """Trello boards requests
    """
    
    @staticmethod
    def manage_board(method, id="", **kwargs):
        """Manage Board

        Args:
            id (str): board id
            method (str): get, update, delete, create
        """
        instance = RequestManager()
        return instance.make_request(http_method=method, endpoint=f"/boards/{id}", **kwargs)
    
    
    @staticmethod
    def create_list(board_id, **kwargs):
        """Create list on Board

        Args:
            board_id (str): board id
        """
        instance = RequestManager()
        return instance.make_request(http_method="post", endpoint=f"/boards/{board_id}/lists", **kwargs)

    @staticmethod
    def get_all_lists(board_id, **kwargs):
        """All lists from the Board

        Args:
            board_id (str): board id
        """
        instance = RequestManager()
        return instance.make_request(http_method="get", endpoint=f"/boards/{board_id}/lists", **kwargs)
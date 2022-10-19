"""Provides a TrelloApiRoutes class to manage endpoints in Trello"""
from enum import Enum


class TrelloApiRoutes(Enum):
    """Trello endpoints enum
    """
    BOARDS = "/members/me/boards"
    BOARD = "/boards/"
    LIST = "/lists"
    LIST_IN_BOARD = "/boards/{}/lists"
    DELETE = "DELETE"

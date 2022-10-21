"""Provides a TrelloApiRoutes class to manage endpoints in Trello"""
from enum import Enum


class TrelloApiRoutes(Enum):
    """Trello endpoints enum
    """
    ORGANIZATIONS = "/organizations"
    MEMBER_IN_ORGANIZATION = "/organizations/{}/members"
    BOARDS = "/members/me/boards"
    BOARD = "/boards/"
    LIST = "/lists"
    LIST_IN_BOARD = "/boards/{}/lists"
    CARDS = "/cards/"
    CARD_IN_BOARD = "/cards/{}/board"
    CARD_IN_LIST = "/cards/{}/list"

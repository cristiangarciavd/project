from enum import Enum


class TrelloApiRoutes(Enum):
    BOARDS = "/members/me/boards"
    BOARD = "/boards/"
    LIST = "/lists"
    DELETE = "DELETE"

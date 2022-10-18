from main.trello.api.trello_boards import TrelloBoard
from main.trello.api.trello_lists import TrelloList

manage_boards = TrelloBoard()
#my_boards = manage_boards.get_all_boards()
#my_boards = manage_boards.get_board("63487163418cdc00401f96d0")
#my_boards = manage_boards.create_board("createTest")
#my_boards = manage_boards.update_board("634ed07927df5904ec75ae6e",name= "pruebaUpdate")
#my_boards = manage_boards.delete_board("634895076b016e01cdcc9a2a")

manage_lists = TrelloList()
my_list = manage_lists.create_list("63487163418cdc00401f96d0", "testList")
my_list = manage_lists.get_all_list("63487163418cdc00401f96d0")

#print(my_boards)
print(my_list)
from main.trello.api.trello_boards import TrelloBoard

# #create new board
req1 = TrelloBoard.manage_board(method="post", name = 'New_Board_Z')

# # update other board
req2 = TrelloBoard.manage_board(method="put", id="9JVb5FpV", name = 'Change_Name_v2')



from request_manager import RequestManager


trelloOb = RequestManager()

trelloOb.make_request(http_method="post", endpoint="/cards", idList= "6346fc12eebb20006f1ddce3",
name= "New Card 700",
desc= "Testing Card",
pos = "top")
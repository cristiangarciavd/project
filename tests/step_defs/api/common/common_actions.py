"""
This module contains step definitions for trello api actions.
"""
from pytest_bdd import given, parsers, when
from sttable import parse_str_table
from main.core.api.request_manager import RequestManager
from main.core.utils.parse_request_body import ParseRequestBody
from main.core.utils.string_utils import StringUtils


@given(parsers.parse("the following body parameters:\n{body}"))
def step_set_body_parameters(datatable, body, request):
    """set body parameters

    Args:
        datatable (datatable): kind of class object to interact with datatables
        body (datatable): body datatable composed by keys and values
        request (object): request fixture object
    """
    datatable.body = parse_str_table(body)
    body = ParseRequestBody.generate_data(datatable.body.rows, request)
    request.body = body


@when(parsers.parse('a "{http_method}" request to "{endpoint}" is send'))
def step_make_request(http_method, request, endpoint):
    """Do request to the cards endpoint
    Args:
        http_method (string): http method or verb
        request (request): request fixture object
        card_name (string): name of the card
    """
    endpoint = StringUtils.replace_tag(endpoint, request)
    response, s_code = RequestManager.get_instance().make_request(
        http_method,
        endpoint,
        payload=request.body
    )
    request.response = response
    request.context["s_code"] = s_code

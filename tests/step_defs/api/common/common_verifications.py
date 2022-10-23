"""
This module contains step definitions for trello api actions.
"""
import jsonschema
from pytest_bdd import then, parsers
from sttable import parse_str_table
from main.core.utils.json_reader import JsonReader
from main.core.utils.parse_request_body import ParseRequestBody 

@then(parsers.parse('the response status code should be "{status_code}"'))
def trelo_card_verify_status(request, status_code):
    """Status code verification

    Args:
        request (request): request fixture object
        status_code (string): status code
    """
    assert str(request.context["s_code"]) == status_code
    
@then(parsers.parse('the "{variable}" of the "{feature}" should be "{value}"'))
def trelo_card_verify_update(request, variable, value):
    """Update variable verification

    Args:
        request (request): request fixture object
        variable (string): value to assert
        value (string): value to assert
    """
    assert request.response[f'{variable}'] == value
    
@then(parsers.parse('the body of the "{feature}" should contain:\n{body}'))
def trelo_card_verify_update(request, datatable, body):
    """Update body verification

    Args:
        request (request): request fixture object
        card_name (string): name of the card
    """
    datatable.body = parse_str_table(body)
    body = ParseRequestBody.generate_data(datatable.body.rows, request)
    assert body == request.body 
    
@then(parsers.parse('the response schema should be verified with "{json_template}"'))
def step_verify_response_schema(json_template, request):  # pylint: disable=W0613
    """verify response schema

    Args:
        json_template (json): schema in json format
        request (request): request fixture object
    """
    base_path = "./main/trello/api/resources/response_schemas/"
    template = JsonReader.get_json(f"{base_path}{json_template}")
    
    try:
            jsonschema.validate(instance=request.response, schema=template)
            verification = True, "Schema successfully verified"
    except jsonschema.exceptions.ValidationError as err:
            verification = False, str(err)
    assert verification[0] == True
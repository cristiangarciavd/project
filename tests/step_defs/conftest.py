"""This module contains shared fixtures, steps, and hooks.
"""
import pytest
from main.core.utils.json_reader import JsonReader
from main.core.api.request_manager import RequestManager
from main.core.api.http_methods import HttpMethods
from main.trello.api.trello_cards import TrelloCard
from main.logger.logger import get_logger


def pytest_bdd_before_scenario(request, feature, scenario):  # pylint: disable=W0613
    """ pytest bdd before scenario

    Parameters
    ----------
        request (object): request object of fixture
        feature (object): feature object of pytest bdd
        scenario (object): scenario object of pytest bdd
    """
    get_logger().info("STARTED SCENARIO %s", scenario.name)
    request.context = {}
    request.tags = []
    request.body = {}
    request.response = {}
    scenario_tags = list(scenario.tags)
    get_logger().info("TAGS %s", scenario.tags)
    
    trello_mods = ["organizations", "boards", "lists", "cards"]
    for mod in trello_mods:
        if f"fixture_create_{mod}" in scenario_tags:
            mods_creation_lvl = trello_mods.index(mod)
            
    
    if mods_creation_lvl >= 0:
        get_logger().info("=> PRE CONDITION STAGE fixture_create_organizations")
        payload = JsonReader.get_json(
            "./main/trello/api/resources/payload_organizations_creation.json")
        response, _ = RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            "/organizations",
            payload=payload
        )
        get_logger().debug('Response:\n%s', response)
        request.context["organizations"] = response
        
    if mods_creation_lvl >= 1:
        get_logger().info("=> PRE CONDITION STAGE fixture_create_boards")
        payload = JsonReader.get_json(
            "./main/trello/api/resources/payload_boards_creation.json")
        payload['idOrganization']= request.context["organizations"]["id"]
        response, _ = RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            "/boards",
            payload=payload
        )
        get_logger().debug('Response:\n%s', response)
        request.context["boards"] = response
    
    if mods_creation_lvl >= 2:
        get_logger().info("=> PRE CONDITION STAGE fixture_create_lists")
        payload = JsonReader.get_json(
            "./main/trello/api/resources/payload_lists_creation.json")
        payload['idBoard']= request.context["boards"]["id"]
        response, _ = RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            "/lists",
            payload=payload
        )
        get_logger().debug('Response:\n%s', response)
        request.context["lists"] = response
    
    if mods_creation_lvl >= 3:
        get_logger().info("=> PRE CONDITION STAGE fixture_create_cards")
        payload = JsonReader.get_json(
            "./main/trello/api/resources/payload_cards_creation.json")
        idList = request.context["lists"]["id"]
        response, _ = TrelloCard.create_card(idList, payload=payload)
        get_logger().debug('Response:\n%s', response)
        request.context["cards"] = response


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):  # noqa:E501  pylint: disable=W0613
    """ pytest bdd step error

    Args:
        multiple args related with pytest bdd
    """
    get_logger().error(f"===>>> FAILED STEP: {step}")


def pytest_bdd_after_scenario(request, feature, scenario):  # pylint: disable=W0613
    """ pytest bdd after scenario

    Args:
        request (object): request object of fixture
        feature (object): feature object of pytest bdd
        scenario (object): scenario object of pytest bdd
    """
    scenario_tags = list(scenario.tags)
    trello_mods = ["cards", "lists", "boards", "organizations"]
    for mod in trello_mods:
        if f"fixture_delete_{mod}" in scenario_tags:
            get_logger().info("=> CLEAN UP STAGE")
            element_id = request.context[f"{mod}"]["id"]
            RequestManager.get_instance().make_request(
                HttpMethods.DELETE.value,
                f"/{mod}/{element_id}")
            get_logger().info("-----------------")

    get_logger().info(
        f"===>>> FINISHED SCENARIO {scenario.name} WITH STATUS: {'FAILED' if scenario.failed else 'SUCCESS'}\n")

@pytest.fixture()
def datatable():
    """fixture to support implementation of datatables

    Returns:
        DataTable
    """
    return DataTable()


class DataTable:
    """Datatable Class to manage table elements
    """

    def __init__(self):
        pass

    def __str__(self):
        dt_str = ''
        for field, value in self.__dict__.items():
            dt_str = f'{dt_str}\n{field} = {value}'
        return dt_str

    def __repr__(self) -> str:
        """
        __repr__
        :return:
        """
        return self.__str__()
"""This module contains shared fixtures, steps, and hooks.
"""
import pytest
from main.core.utils.json_reader import JsonReader
from main.core.api.request_manager import RequestManager
from main.core.api.http_methods import HttpMethods
from main.logger.logger import wrap, get_logger, entering, exiting

@pytest.fixture(autouse=True, scope="module")
def setup(request):
    """context of before all
    """

    get_logger().info("======>>> EXECUTED BEFORE ALL <<<======\n")

    def pytest_bdd_after_all():
        get_logger().info("======>>> EXECUTED AFTER ALL  <<<======\n")
    request.addfinalizer(pytest_bdd_after_all)


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
    
    if "fixture_create_organizations" in scenario_tags:
        get_logger().info("=> PRE CONDITION STAGE fixture_create_organizations")
        payload = JsonReader.get_json(
            "./main/trello/api/resources/payload_organizations_creation.json")
        response, _ = RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            "/organizations",
            payload=payload
        )
        get_logger().info('Response:\n%s', response)
        request.context["organizations"] = response
        
    if "fixture_create_boards" in scenario_tags:
        get_logger().info("=> PRE CONDITION STAGE fixture_create_boards")
        payload = JsonReader.get_json(
            "./main/trello/api/resources/payload_boards_creation.json")
        payload['idOrganization']= request.context["organizations"]["id"]
        response, _ = RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            "/boards",
            payload=payload
        )
        get_logger().info('Response:\n%s', response)
        request.context["boards"] = response
    
    if "fixture_create_lists" in scenario_tags:
        get_logger().info("=> PRE CONDITION STAGE fixture_create_lists")
        payload = JsonReader.get_json(
            "./main/trello/api/resources/payload_lists_creation.json")
        payload['idBoard']= request.context["boards"]["id"]
        response, _ = RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            "/lists",
            payload=payload
        )
        get_logger().info('Response:\n%s', response)
        request.context["lists"] = response
    
    if "fixture_create_cards" in scenario_tags:
        get_logger().info("=> PRE CONDITION STAGE fixture_create_cards")
        payload = JsonReader.get_json(
            "./main/trello/api/resources/payload_cards_creation.json")
        payload['idList'] = request.context["lists"]["id"]
        response, _ = RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            "/cards",
            payload=payload
        )
        get_logger().info('Response:\n%s', response)
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

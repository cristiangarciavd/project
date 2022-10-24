"""
This module contains step definitions for trello_api_cards.feature.
"""
from pytest_bdd import scenarios
from tests.step_defs.api.common.common_actions import *  # noqa:F401 F403 E501 pylint: disable=W0401 W0614
from tests.step_defs.api.common.common_verifications import *  # noqa:F401 F403 E501 pylint: disable=W0401 W0614

scenarios("../features/api/")

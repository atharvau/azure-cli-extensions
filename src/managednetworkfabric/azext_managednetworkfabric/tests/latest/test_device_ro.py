# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# --------------------------------------------------------------------------------------------
# pylint: disable=too-few-public-methods,unnecessary-pass,unused-argument

<<<<<<< HEAD
=======
import json
>>>>>>> upstream/main
from azure.cli.testsdk.scenario_tests import AllowLargeResponse

"""
Device tests scenarios
"""

from azure.cli.testsdk import ScenarioTest

from .config import CONFIG


<<<<<<< HEAD
def setup_scenario1(test):
=======
def setup_scenario(test):
>>>>>>> upstream/main
    """Env setup_scenario1"""
    pass


<<<<<<< HEAD
def cleanup_scenario1(test):
=======
def cleanup_scenario(test):
>>>>>>> upstream/main
    """Env cleanup_scenario1"""
    pass


def call_scenario1(test):
    """# Testcase: scenario1"""
<<<<<<< HEAD
    setup_scenario1(test)
    step_ro(test, checks=[])
    cleanup_scenario1(test)


def step_ro(test, checks=None):
    """Device run RO operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric device run-ro --resource-name {name} --resource-group {rg} --ro-command {command}"
=======
    setup_scenario(test)
    step_ro_valid_json(test, checks=[])
    cleanup_scenario(test)


def call_scenario2(test):
    """# Testcase: scenario2"""
    setup_scenario(test)
    step_ro_invalid_json(test, checks=[])
    cleanup_scenario(test)


def step_ro_valid_json(test, checks=None):
    """Device run RO operation - valid JSON"""
    if checks is None:
        checks = []
    output = test.cmd(
        "az networkfabric device run-ro --resource-name {name} --resource-group {rg} --ro-command {command}"
    ).get_output_in_json()

    expected_object = {
        "configurationState": CONFIG.get("NETWORK_DEVICE", "ro_config_state"),
        "outputUrl": CONFIG.get("NETWORK_DEVICE", "ro_output_url"),
        "deviceConfigurationPreview": {
            "architecture": "x86_64",
            "bootupTimestamp": 1708977169.5043042,
            "configMacAddress": "00:00:00:00:00:00",
        },
    }

    assert output == expected_object


def step_ro_invalid_json(test, checks=None):
    """Device run RO operation - Invalid  JSON - truncated at server"""
    if checks is None:
        checks = []
    output = test.cmd(
        "az networkfabric device run-ro --resource-name {name} --resource-group {rg} --ro-command {command}"
    ).get_output_in_json()

    expected_object = {
        "configurationState": CONFIG.get("NETWORK_DEVICE", "ro_config_state"),
        "outputUrl": CONFIG.get("NETWORK_DEVICE", "ro_output_url"),
        "deviceConfigurationPreview": '{\n  "architecture": "x86_64",\n  "bootupTimestamp": 1708977169.5043042,\n  "configMacAddr',
    }

    assert output == expected_object
    assert (
        output["deviceConfigurationPreview"]
        == expected_object["deviceConfigurationPreview"]
>>>>>>> upstream/main
    )


class GA_DeviceRoScenarioTest1(ScenarioTest):
    """DeviceScenario test"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs.update(
            {
                "name": CONFIG.get("NETWORK_DEVICE", "ro_device_name"),
                "rg": CONFIG.get("NETWORK_DEVICE", "ro_device_rg"),
                "command": CONFIG.get("NETWORK_DEVICE", "ro_command"),
            }
        )

    @AllowLargeResponse()
    def test_GA_Device_Ro_scenario1(self):
<<<<<<< HEAD
        """test scenario for Device CRUD operations"""
        call_scenario1(self)
=======
        """test scenario for Device CRUD operations - valid JSON"""
        call_scenario1(self)


class GA_DeviceRoScenarioTest2(ScenarioTest):
    """DeviceScenario test"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs.update(
            {
                "name": CONFIG.get("NETWORK_DEVICE", "ro_device_name"),
                "rg": CONFIG.get("NETWORK_DEVICE", "ro_device_rg"),
                "command": CONFIG.get("NETWORK_DEVICE", "ro_command"),
            }
        )

    @AllowLargeResponse()
    def test_GA_Device_Ro_scenario2(self):
        """test scenario for Device CRUD operations - invalid JSON"""
        call_scenario2(self)
>>>>>>> upstream/main

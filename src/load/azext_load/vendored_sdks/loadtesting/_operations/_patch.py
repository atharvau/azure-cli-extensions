<<<<<<< HEAD
=======
# pylint: disable=line-too-long,useless-suppression
>>>>>>> upstream/main
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
<<<<<<< HEAD
from typing import List

"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
import logging
import time
from functools import partial
from typing import List, IO, Optional, Any, Union, overload, Generic, TypeVar

from azure.core.polling import PollingMethod
from azure.core.tracing.decorator import distributed_trace
from azure.core.polling import LROPoller

from ._operations import (
    LoadTestAdministrationClientOperationsMixin as AdministrationOperationsGenerated,
    JSON,
)
from ._operations import LoadTestRunClientOperationsMixin as TestRunOperationsGenerated
from .._serialization import Serializer
from .. import models as _models

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

=======
import logging
import time
from functools import partial
from typing import Any, IO, List, Optional, overload, Union

from azure.core.polling import PollingMethod, LROPoller
from azure.core.tracing.decorator import distributed_trace

from ._operations import JSON
from ._operations import LoadTestAdministrationClientOperationsMixin as GeneratedAdministrationClientOperations
from ._operations import LoadTestRunClientOperationsMixin as GeneratedRunClientOperations

from .. import models as _models

>>>>>>> upstream/main
logger = logging.getLogger(__name__)


class LoadTestingPollingMethod(PollingMethod):
    """Base class for custom sync polling methods."""

    def _update_status(self) -> None:
        raise NotImplementedError("This method needs to be implemented")

    def _update_resource(self) -> None:
        self._resource = self._command()

    def initialize(self, client, initial_response, deserialization_callback) -> None:
        self._command = client
        self._initial_response = initial_response
        self._resource = initial_response

    def status(self) -> str:
        return self._status

    def finished(self) -> bool:
        return self._status in self._termination_statuses

    def resource(self) -> JSON:
        return self._resource

    def run(self) -> None:
        try:
            while not self.finished():
                self._update_resource()
                self._update_status()

                if not self.finished():
                    time.sleep(self._polling_interval)
        except Exception as e:
            logger.error(e)
            raise e


class ValidationCheckPoller(LoadTestingPollingMethod):
<<<<<<< HEAD
    """polling method for long-running validation check operation."""
=======
    """Polling method for long-running file validation operation."""
>>>>>>> upstream/main

    def __init__(self, interval=5) -> None:
        self._resource = None
        self._command = None
        self._initial_response = None
        self._polling_interval = interval
        self._status = None
        self._termination_statuses = [
<<<<<<< HEAD
            "NOT_VALIDATED",
            "VALIDATION_SUCCESS",
            "VALIDATION_FAILURE",
=======
            "VALIDATION_SUCCESS",
            "VALIDATION_FAILURE",
            "NOT_VALIDATED",
>>>>>>> upstream/main
            "VALIDATION_NOT_REQUIRED",
        ]

    def _update_status(self) -> None:
        self._status = self._resource["validationStatus"]


class TestRunStatusPoller(LoadTestingPollingMethod):
<<<<<<< HEAD
=======
    """Polling method for polling a Test Run."""

>>>>>>> upstream/main
    def __init__(self, interval=5) -> None:
        self._resource = None
        self._command = None
        self._initial_response = None
        self._polling_interval = interval
        self._status = None
        self._termination_statuses = ["DONE", "FAILED", "CANCELLED"]

    def _update_status(self) -> None:
        self._status = self._resource["status"]


<<<<<<< HEAD
class LoadTestAdministrationClientOperationsMixin(AdministrationOperationsGenerated):
    """
    for performing the operations on the Administration Subclient
    """
=======
class TestProfileRunStatusPoller(LoadTestingPollingMethod):
    """Polling method for polling a Test Profile Run."""

    def __init__(self, interval=5) -> None:
        self._resource = None
        self._command = None
        self._initial_response = None
        self._polling_interval = interval
        self._status = None
        self._termination_statuses = ["DONE", "FAILED", "CANCELLED"]

    def _update_status(self):
        self._status = self._resource["status"]


class LoadTestAdministrationClientOperationsMixin(GeneratedAdministrationClientOperations):
>>>>>>> upstream/main

    def __init__(self, *args, **kwargs):
        super(LoadTestAdministrationClientOperationsMixin, self).__init__(*args, **kwargs)

<<<<<<< HEAD
    @distributed_trace
    def begin_upload_test_file(
        self, test_id: str, file_name: str, body: IO, *, file_type: Optional[str] = None, **kwargs: Any
    ) -> LROPoller[JSON]:
        """Upload file to the test

        :param test_id: Unique id for the test
        :type test_id: str
        :param file_name: Name of the file to be uploaded
        :type file_name: str
        :param body: File content to be uploaded
        :type body: IO
        :param file_type: Type of the file to be uploaded
        :type file_type: str
        :return: An instance of LROPoller object to check the validation status of file
        :rtype: ~azure.developer.loadtesting._polling.LoadTestingLROPoller
        :raises ~azure.core.exceptions.HttpResponseError:
        :raises ~azure.core.exceptions.ResourceNotFoundError:
=======
    @overload
    def begin_upload_test_file(
        self,
        test_id: str,
        file_name: str,
        body: bytes,
        *,
        file_type: Optional[Union[str, _models.FileType]] = None,
        **kwargs: Any
    ) -> LROPoller[_models.TestFileInfo]:
        """Upload input file for a given test Id. File size can't be more than 50 MB.
        Existing file with same name for the given test will be overwritten. File
        should be provided in the request body as application/octet-stream.

        Upload input file for a given test Id. File size can't be more than 50 MB.
        Existing file with same name for the given test will be overwritten. File
        should be provided in the request body as application/octet-stream.

        :param test_id: Unique name for the load test, must contain only lower-case alphabetic,
         numeric, underscore or hyphen characters. Required.
        :type test_id: str
        :param file_name: Unique name for test file with file extension like : App.jmx. Required.
        :type file_name: str
        :param body: The file content as application/octet-stream. Required.
        :type body: bytes
        :keyword file_type: File type. Known values are: "JMX_FILE", "USER_PROPERTIES",
         "ADDITIONAL_ARTIFACTS", "ZIPPED_ARTIFACTS", "URL_TEST_CONFIG", and "TEST_SCRIPT". Default value
         is None.
        :paramtype file_type: str or ~azure.developer.loadtesting.models.FileType
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestFileInfo`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestFileInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_upload_test_file(
        self,
        test_id: str,
        file_name: str,
        body: IO,
        *,
        file_type: Optional[Union[str, _models.FileType]] = None,
        **kwargs: Any
    ) -> LROPoller[_models.TestFileInfo]:
        """Upload input file for a given test Id. File size can't be more than 50 MB.
        Existing file with same name for the given test will be overwritten. File
        should be provided in the request body as application/octet-stream.

        Upload input file for a given test Id. File size can't be more than 50 MB.
        Existing file with same name for the given test will be overwritten. File
        should be provided in the request body as application/octet-stream.

        :param test_id: Unique name for the load test, must contain only lower-case alphabetic,
         numeric, underscore or hyphen characters. Required.
        :type test_id: str
        :param file_name: Unique name for test file with file extension like : App.jmx. Required.
        :type file_name: str
        :param body: The file content as application/octet-stream. Required.
        :type body: IO
        :keyword file_type: File type. Known values are: "JMX_FILE", "USER_PROPERTIES",
         "ADDITIONAL_ARTIFACTS", "ZIPPED_ARTIFACTS", "URL_TEST_CONFIG", and "TEST_SCRIPT". Default value
         is None.
        :paramtype file_type: str or ~azure.developer.loadtesting.models.FileType
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestFileInfo`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestFileInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_upload_test_file(
        self,
        test_id: str,
        file_name: str,
        body: Union[IO, bytes],
        *,
        file_type: Optional[Union[str, _models.FileType]] = None,
        **kwargs: Any
    ) -> LROPoller[_models.TestFileInfo]:
        """Upload input file for a given test Id. File size can't be more than 50 MB.
        Existing file with same name for the given test will be overwritten. File
        should be provided in the request body as application/octet-stream.

        Upload input file for a given test Id. File size can't be more than 50 MB.
        Existing file with same name for the given test will be overwritten. File
        should be provided in the request body as application/octet-stream.

        :param test_id: Unique name for the load test, must contain only lower-case alphabetic,
         numeric, underscore or hyphen characters. Required.
        :type test_id: str
        :param file_name: Unique name for test file with file extension like : App.jmx. Required.
        :type file_name: str
        :param body: The file content as application/octet-stream. Required.
        :type body: Is one of the following types: IO, bytes
        :keyword file_type: File type. Known values are: "JMX_FILE", "USER_PROPERTIES",
         "ADDITIONAL_ARTIFACTS", "ZIPPED_ARTIFACTS", "URL_TEST_CONFIG", and "TEST_SCRIPT". Default value
         is None.
        :paramtype file_type: str or ~azure.developer.loadtesting.models.FileType
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestFileInfo`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestFileInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
>>>>>>> upstream/main
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
<<<<<<< HEAD
        upload_test_file_operation = super().begin_upload_test_file(
            test_id=test_id, file_name=file_name, body=body, file_type=file_type, **kwargs
        )

        command = partial(self.get_test_file, test_id=test_id, file_name=file_name)

        create_validation_status_polling = ValidationCheckPoller(interval=polling_interval)
        return LROPoller(
            command,
            upload_test_file_operation,
            lambda *_: None,
            create_validation_status_polling,
        )


class LoadTestRunClientOperationsMixin(TestRunOperationsGenerated):
    """
    class to perform operations on TestRun
    """
=======
        upload_test_file_operation = super()._begin_upload_test_file(
            test_id=test_id, file_name=file_name, file_type=file_type, body=body, **kwargs
        )

        command = partial(self.get_test_file, test_id=test_id, file_name=file_name)
        file_validation_status_polling = ValidationCheckPoller(interval=polling_interval)
        return LROPoller(command, upload_test_file_operation, lambda *_: None, file_validation_status_polling)


class LoadTestRunClientOperationsMixin(GeneratedRunClientOperations):
>>>>>>> upstream/main

    def __init__(self, *args, **kwargs):
        super(LoadTestRunClientOperationsMixin, self).__init__(*args, **kwargs)

    @overload
<<<<<<< HEAD
=======
    def begin_test_run(
        self,
        test_run_id: str,
        body: _models.TestRun,
        *,
        content_type: str = "application/merge-patch+json",
        old_test_run_id: Optional[str] = None,
        **kwargs: Any
    ) -> LROPoller[_models.TestRun]:
        """Create and start a new test run with the given test run Id.

        Create and start a new test run with the given test run Id.

        :param test_run_id: Unique test run identifier for the load test run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_run_id: str
        :param body: The resource instance. Required.
        :type body: ~azure.developer.loadtesting.models.TestRun
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :keyword old_test_run_id: Existing test run identifier that should be rerun, if this is
         provided, the
         test will run with the JMX file, configuration and app components from the
         existing test run. You can override the configuration values for new test run
         in the request body. Default value is None.
        :paramtype old_test_run_id: str
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestRun`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestRun]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_test_run(
        self,
        test_run_id: str,
        body: JSON,
        *,
        content_type: str = "application/merge-patch+json",
        old_test_run_id: Optional[str] = None,
        **kwargs: Any
    ) -> LROPoller[_models.TestRun]:
        """Create and start a new test run with the given test run Id.

        Create and start a new test run with the given test run Id.

        :param test_run_id: Unique test run identifier for the load test run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_run_id: str
        :param body: The resource instance. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :keyword old_test_run_id: Existing test run identifier that should be rerun, if this is
         provided, the
         test will run with the JMX file, configuration and app components from the
         existing test run. You can override the configuration values for new test run
         in the request body. Default value is None.
        :paramtype old_test_run_id: str
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestRun`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestRun]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_test_run(
        self,
        test_run_id: str,
        body: IO[bytes],
        *,
        content_type: str = "application/merge-patch+json",
        old_test_run_id: Optional[str] = None,
        **kwargs: Any
    ) -> LROPoller[_models.TestRun]:
        """Create and start a new test run with the given test run Id.

        Create and start a new test run with the given test run Id.

        :param test_run_id: Unique test run identifier for the load test run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_run_id: str
        :param body: The resource instance. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :keyword old_test_run_id: Existing test run identifier that should be rerun, if this is
         provided, the
         test will run with the JMX file, configuration and app components from the
         existing test run. You can override the configuration values for new test run
         in the request body. Default value is None.
        :paramtype old_test_run_id: str
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestRun`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestRun]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_test_run(
        self,
        test_run_id: str,
        body: Union[_models.TestRun, JSON, IO[bytes]],
        *,
        old_test_run_id: Optional[str] = None,
        **kwargs: Any
    ) -> LROPoller[_models.TestRun]:
        """Create and start a new test run with the given test run Id.

        Create and start a new test run with the given test run Id.

        :param test_run_id: Unique test run identifier for the load test run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_run_id: str
        :param body: The resource instance. Is one of the following types: TestRun, JSON, IO[bytes]
         Required.
        :type body: ~azure.developer.loadtesting.models.TestRun or JSON or IO[bytes]
        :keyword old_test_run_id: Existing test run identifier that should be rerun, if this is
         provided, the
         test will run with the JMX file, configuration and app components from the
         existing test run. You can override the configuration values for new test run
         in the request body. Default value is None.
        :paramtype old_test_run_id: str
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestRun`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestRun]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5

        create_or_update_test_run_operation = super()._begin_test_run(
            test_run_id, body, old_test_run_id=old_test_run_id, **kwargs
        )
        command = partial(self.get_test_run, test_run_id=test_run_id)

        test_run_status_polling = TestRunStatusPoller(interval=polling_interval)
        return LROPoller(
            command,
            create_or_update_test_run_operation,
            lambda *_: None,
            test_run_status_polling,
        )

    @overload
>>>>>>> upstream/main
    def begin_test_profile_run(
        self,
        test_profile_run_id: str,
        body: _models.TestProfileRun,
        *,
<<<<<<< HEAD
        content_type: Optional[str] = None,
        **kwargs: Any
    ) -> LROPoller[JSON]:
=======
        content_type: str = "application/merge-patch+json",
        **kwargs: Any
    ) -> LROPoller[_models.TestProfileRun]:
>>>>>>> upstream/main
        """Create and start a new test profile run.

        Create and start a new test profile run with the given test profile run Id.

        :param test_profile_run_id: Unique identifier for the test profile run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_profile_run_id: str
        :param body: The resource instance. Required.
        :type body: ~azure.developer.loadtesting.models.TestProfileRun
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
<<<<<<< HEAD

        :return: TestProfileRun. The TestProfileRun is compatible with MutableMapping
        :rtype: ~azure.developer.loadtesting.models.TestProfileRun
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_profile_run_operation = super().begin_test_profile_run(
            test_profile_run_id, body, content_type=content_type, **kwargs
        )
        command = partial(self.get_test_profile_run, test_profile_run_id=test_profile_run_id)

        create_test_profile_run_polling = TestRunStatusPoller(interval=polling_interval)
        return LROPoller(
            command,
            create_or_update_test_profile_run_operation,
            lambda *_: None,
            create_test_profile_run_polling,
        )

    @overload
    def begin_test_profile_run(
        self, test_profile_run_id: str, body: JSON, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> LROPoller[JSON]:
=======
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestProfileRun`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestProfileRun]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_test_profile_run(
        self, test_profile_run_id: str, body: JSON, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> LROPoller[_models.TestProfileRun]:
>>>>>>> upstream/main
        """Create and start a new test profile run.

        Create and start a new test profile run with the given test profile run Id.

        :param test_profile_run_id: Unique identifier for the test profile run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_profile_run_id: str
        :param body: The resource instance. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
<<<<<<< HEAD

        :return: TestProfileRun. The TestProfileRun is compatible with MutableMapping
        :rtype: ~azure.developer.loadtesting.models.TestProfileRun
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_profile_run_operation = super().begin_test_profile_run(
            test_profile_run_id, body, content_type=content_type, **kwargs
        )
        command = partial(self.get_test_profile_run, test_profile_run_id=test_profile_run_id)

        create_test_profile_run_polling = TestRunStatusPoller(interval=polling_interval)
        return LROPoller(
            command,
            create_or_update_test_profile_run_operation,
            lambda *_: None,
            create_test_profile_run_polling,
        )

    @overload
    def begin_test_profile_run(
        self, test_profile_run_id: str, body: IO[bytes], *, content_type: Optional[str] = None, **kwargs: Any
    ) -> LROPoller[JSON]:
        """Create and start a new test profile run.

        Create and start a new test profile run with the given test profile run Id.

        :param test_profile_run_id: Unique identifier for the test profile run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_profile_run_id: str
        :param body: The resource instance. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str

        :return: TestProfileRun. The TestProfileRun is compatible with MutableMapping
        :rtype: ~azure.developer.loadtesting.models.TestProfileRun
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_profile_run_operation = super().begin_test_profile_run(
            test_profile_run_id, body, content_type=content_type, **kwargs
        )
        command = partial(self.get_test_profile_run, test_profile_run_id=test_profile_run_id)

        create_test_profile_run_polling = TestRunStatusPoller(interval=polling_interval)
        return LROPoller(
            command,
            create_or_update_test_profile_run_operation,
            lambda *_: None,
            create_test_profile_run_polling,
        )

    @distributed_trace
    def begin_test_profile_run(
        self,
        test_profile_run_id: str,
        body: Union[_models.TestProfileRun, JSON, IO[bytes]],
        *,
        content_type: Optional[str] = None,
        **kwargs: Any
    ) -> LROPoller[JSON]:
=======
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestProfileRun`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestProfileRun]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_test_profile_run(
        self,
        test_profile_run_id: str,
        body: IO[bytes],
        *,
        content_type: str = "application/merge-patch+json",
        **kwargs: Any
    ) -> LROPoller[_models.TestProfileRun]:
>>>>>>> upstream/main
        """Create and start a new test profile run.

        Create and start a new test profile run with the given test profile run Id.

        :param test_profile_run_id: Unique identifier for the test profile run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_profile_run_id: str
        :param body: The resource instance. Required.
<<<<<<< HEAD
        :type body: ~azure.developer.loadtesting.models.TestProfileRun or JSON or IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str

        :return: TestProfileRun. The TestProfileRun is compatible with MutableMapping
        :rtype: ~azure.developer.loadtesting.models.TestProfileRun
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_profile_run_operation = super().begin_test_profile_run(
            test_profile_run_id, body, content_type=content_type, **kwargs
        )
        command = partial(self.get_test_profile_run, test_profile_run_id=test_profile_run_id)

        create_test_profile_run_polling = TestRunStatusPoller(interval=polling_interval)
=======
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: TestProfileRun. The TestProfileRun is compatible with MutableMapping
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestProfileRun`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestProfileRun]
        """

    @distributed_trace
    def begin_test_profile_run(
        self, test_profile_run_id: str, body: Union[_models.TestProfileRun, JSON, IO[bytes]], **kwargs: Any
    ) -> LROPoller[_models.TestProfileRun]:
        """Create and start a new test profile run.

        Create and start a new test profile run with the given test profile run Id.

        :param test_profile_run_id: Unique identifier for the test profile run, must contain only
         lower-case alphabetic, numeric, underscore or hyphen characters. Required.
        :type test_profile_run_id: str
        :param body: The resource instance. Is one of the following types: TestProfileRun, JSON,
         IO[bytes] Required.
        :type body: ~azure.developer.loadtesting.models.TestProfileRun or JSON or IO[bytes]
        :return: An instance of LROPoller. Call `result()` on the poller object to return a :class:`~azure.developer.loadtesting.models.TestProfileRun`.
        :rtype: ~azure.core.polling.LROPoller[~azure.developer.loadtesting.models.TestProfileRun]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_profile_run_operation = super()._begin_test_profile_run(
            test_profile_run_id, body, **kwargs
        )
        command = partial(self.get_test_profile_run, test_profile_run_id=test_profile_run_id)

        test_profile_run_status_polling = TestProfileRunStatusPoller(interval=polling_interval)
>>>>>>> upstream/main
        return LROPoller(
            command,
            create_or_update_test_profile_run_operation,
            lambda *_: None,
<<<<<<< HEAD
            create_test_profile_run_polling,
        )

    @overload
    def begin_test_run(
        self, test_run_id: str, body: _models.TestRun, *, old_test_run_id: Optional[str] = None, **kwargs: Any
    ) -> LROPoller[JSON]:
        """Create and start a new test run with the given name.

        Create and start a new test run with the given name.

        :param test_run_id: Unique name for the load test run, must contain only lower-case alphabetic,
         numeric, underscore or hyphen characters. Required.
        :type test_run_id: str
        :param body: The resource instance. Required.
        :type body:  ~azure.developer.loadtesting.models.TestRun
        :keyword old_test_run_id: Existing test run identifier that should be rerun, if this is
         provided, the test will run with the JMX file, configuration and app components from the
         existing test run. You can override the configuration values for new test run in the request
         body. Default value is None.
        :paramtype old_test_run_id: str
        :keyword content_type: Body Parameter content-type. Known values are:
         'application/merge-patch+json'. Default value is None.
        :paramtype content_type: str

        :rtype: ~azure.developer.loadtesting._polling.LoadTestingLROPoller
        :raises ~azure.core.exceptions.HttpResponseError:
        :raises ~azure.core.exceptions.ResourceNotFoundError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_run_operation = super().begin_test_run(
            test_run_id, body, old_test_run_id=old_test_run_id, **kwargs
        )
        logger.info(isinstance(create_or_update_test_run_operation, _models.TestRun))
        command = partial(self.get_test_run, test_run_id=test_run_id)

        create_test_run_polling = TestRunStatusPoller(interval=polling_interval)
        return LROPoller(
            command,
            create_or_update_test_run_operation,
            lambda *_: None,
            create_test_run_polling,
        )

    @overload
    def begin_test_run(
        self, test_run_id: str, body: JSON, *, old_test_run_id: Optional[str] = None, **kwargs: Any
    ) -> LROPoller[JSON]:
        """Create and start a new test run with the given name.

        Create and start a new test run with the given name.

        :param test_run_id: Unique name for the load test run, must contain only lower-case alphabetic,
         numeric, underscore or hyphen characters. Required.
        :type test_run_id: str
        :param body: The resource instance. Required.
        :type body: JSON
        :keyword old_test_run_id: Existing test run identifier that should be rerun, if this is
         provided, the test will run with the JMX file, configuration and app components from the
         existing test run. You can override the configuration values for new test run in the request
         body. Default value is None.
        :paramtype old_test_run_id: str
        :keyword content_type: Body Parameter content-type. Known values are:
         'application/merge-patch+json'. Default value is None.
        :paramtype content_type: str

        :rtype: ~azure.developer.loadtesting._polling.LoadTestingLROPoller
        :raises ~azure.core.exceptions.HttpResponseError:
        :raises ~azure.core.exceptions.ResourceNotFoundError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_run_operation = super().begin_test_run(
            test_run_id, body, old_test_run_id=old_test_run_id, **kwargs
        )
        command = partial(self.get_test_run, test_run_id=test_run_id)

        create_test_run_polling = TestRunStatusPoller(interval=polling_interval)
        return LROPoller(
            command,
            create_or_update_test_run_operation,
            lambda *_: None,
            create_test_run_polling,
        )

    @overload
    def begin_test_run(
        self, test_run_id: str, body: IO[bytes], *, old_test_run_id: Optional[str] = None, **kwargs: Any
    ) -> LROPoller[JSON]:
        """Create and start a new test run with the given name.

        Create and start a new test run with the given name.

        :param test_run_id: Unique name for the load test run, must contain only lower-case alphabetic,
         numeric, underscore or hyphen characters. Required.
        :type test_run_id: str
        :param body: The resource instance. Required.
        :type body: IO[bytes]
        :keyword old_test_run_id: Existing test run identifier that should be rerun, if this is
         provided, the test will run with the JMX file, configuration and app components from the
         existing test run. You can override the configuration values for new test run in the request
         body. Default value is None.
        :paramtype old_test_run_id: str
        :keyword content_type: Body Parameter content-type. Known values are:
         'application/merge-patch+json'. Default value is None.
        :paramtype content_type: str

        :rtype: ~azure.developer.loadtesting._polling.LoadTestingLROPoller
        :raises ~azure.core.exceptions.HttpResponseError:
        :raises ~azure.core.exceptions.ResourceNotFoundError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_run_operation = super().begin_test_run(
            test_run_id, body, old_test_run_id=old_test_run_id, **kwargs
        )
        command = partial(self.get_test_run, test_run_id=test_run_id)

        create_test_run_polling = TestRunStatusPoller(interval=polling_interval)
        return LROPoller(
            command,
            create_or_update_test_run_operation,
            lambda *_: None,
            create_test_run_polling,
        )

    @distributed_trace
    def begin_test_run(
        self,
        test_run_id: str,
        body: Union[_models.TestRun, JSON, IO[bytes]],
        *,
        old_test_run_id: Optional[str] = None,
        **kwargs: Any
    ) -> LROPoller[JSON]:
        """Create and start a new test run with the given name.

        Create and start a new test run with the given name.

        :param test_run_id: Unique name for the load test run, must contain only lower-case alphabetic,
         numeric, underscore or hyphen characters. Required.
        :type test_run_id: str
        :param body: The resource instance. Is one of the following types: TestRun, JSON, IO[bytes]
         Required.
        :type body: ~azure.developer.loadtesting.models.TestRun or JSON or IO[bytes]
        :keyword old_test_run_id: Existing test run identifier that should be rerun, if this is
         provided, the test will run with the JMX file, configuration and app components from the
         existing test run. You can override the configuration values for new test run in the request
         body. Default value is None.
        :paramtype old_test_run_id: str
        :keyword content_type: Body Parameter content-type. Known values are:
         'application/merge-patch+json'. Default value is None.
        :paramtype content_type: str

        :rtype: ~azure.developer.loadtesting._polling.LoadTestingLROPoller
        :raises ~azure.core.exceptions.HttpResponseError:
        :raises ~azure.core.exceptions.ResourceNotFoundError:
        """

        polling_interval = kwargs.pop("_polling_interval", None)
        if polling_interval is None:
            polling_interval = 5
        create_or_update_test_run_operation = super().begin_test_run(
            test_run_id, body, old_test_run_id=old_test_run_id, **kwargs
        )
        command = partial(self.get_test_run, test_run_id=test_run_id)

        create_test_run_polling = TestRunStatusPoller(interval=polling_interval)
        return LROPoller(
            command,
            create_or_update_test_run_operation,
            lambda *_: None,
            create_test_run_polling,
        )


__all__: List[str] = [
    "LoadTestAdministrationClientOperationsMixin",
    "LoadTestRunClientOperationsMixin",
]


# Add all objects you want publicly available to users at this package level
=======
            test_profile_run_status_polling,
        )


# Add all objects you want publicly available to users at this package level
__all__: List[str] = ["LoadTestAdministrationClientOperationsMixin", "LoadTestRunClientOperationsMixin"]
>>>>>>> upstream/main


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
<<<<<<< HEAD
from azext_portal.generated._help import helps  # pylint: disable=unused-import
try:
    from azext_portal.manual._help import helps  # pylint: disable=reimported
except ImportError:
    pass
=======
>>>>>>> upstream/main


class PortalCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
<<<<<<< HEAD
        from .generated._client_factory import cf_portal
        portal_custom = CliCommandType(
            operations_tmpl='azext_portal.custom#{}',
            client_factory=cf_portal)
=======
        portal_custom = CliCommandType(
            operations_tmpl='azext_portal.custom#{}'
        )
>>>>>>> upstream/main
        super(PortalCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                   custom_command_type=portal_custom)

    def load_command_table(self, args):
<<<<<<< HEAD
        from .generated.commands import load_command_table
=======
        from azext_portal.commands import load_command_table
        from azure.cli.core.aaz import load_aaz_command_table
        try:
            from . import aaz
        except ImportError:
            aaz = None
        if aaz:
            load_aaz_command_table(
                loader=self,
                aaz_pkg_name=aaz.__name__,
                args=args
            )
>>>>>>> upstream/main
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
<<<<<<< HEAD
        from .generated._params import load_arguments
=======
        from azext_portal._params import load_arguments
>>>>>>> upstream/main
        load_arguments(self, command)


COMMAND_LOADER_CLS = PortalCommandsLoader

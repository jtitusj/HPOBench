import os
import importlib


def __reload_module():
    """
    The env variable which enables the debug level is read in during the import of the client module.
    Reloading the module, re-reads the env variable and therefore changes the level.
    """
    import hpobench.container.client_abstract_benchmark as client
    importlib.reload(client)


def enable_container_debug():
    """ Sets the environment variable "HPOBENCH_DEBUG" to true. The container checks this variable and if set to true,
        enables debugging on the container side. """
    os.environ['HPOBENCH_DEBUG'] = 'true'
    __reload_module()


def disable_container_debug():
    os.environ['HPOBENCH_DEBUG'] = 'false'
    __reload_module()

import importlib.util
import os
from os.path import basename, dirname, isfile, join

for root, dirs, files in os.walk(dirname(__file__)):
    for file_name in files:
        module_path = join(root, file_name)
        if (
            isfile(module_path)
            and not module_path.endswith("__init__.py")
            and module_path.endswith(".py")
        ):
            base_name = basename(module_path)[:-3]
            module_spec = importlib.util.spec_from_file_location(
                base_name, module_path
            )
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)

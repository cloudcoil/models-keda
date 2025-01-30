from types import ModuleType

import cloudcoil.models.keda as keda


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), keda.__dict__.values()))
    assert modules, "No modules found in keda"

# cloudcoil.models.keda

Typed keda resources for the Cloudcoil Kubernetes client.

[![PyPI](https://img.shields.io/pypi/v/cloudcoil.models.keda.svg)](https://pypi.org/project/cloudcoil.models.keda/)
[![CI](https://github.com/cloudcoil/models-keda/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudcoil/models-keda/actions/workflows/ci.yml)

## Install a published release

Requires Python 3.14+:

```sh
uv add cloudcoil.models.keda
# Or:
pip install cloudcoil.models.keda
```

Select a version matching the upstream APIs you use and pin a compatible Cloudcoil
minor. The [versioning guide](https://github.com/cloudcoil/cloudcoil/blob/main/VERSIONING.md)
explains the upstream version and packaging revision. Model installation does not
install Kubernetes or an upstream operator.

Use the [Cloudcoil documentation](https://cloudcoil.github.io/cloudcoil/) for client
operations, controllers and admission. Report generation or packaging problems in
[cloudcoil/cloudcoil](https://github.com/cloudcoil/cloudcoil/issues).

Licensed under [Apache-2.0](https://github.com/cloudcoil/cloudcoil/blob/main/LICENSE).
## KEDA models

Models are generated from pinned upstream schemas. Configuration, schema inputs
and README sources are maintained in
[cloudcoil/cloudcoil](https://github.com/cloudcoil/cloudcoil/tree/main/models/keda);
the generated package is in
[cloudcoil/models-keda](https://github.com/cloudcoil/models-keda). Edit the
source integration in Cloudcoil because generated repository edits are replaced
on template refresh.

### Use a typed resource

After installing `cloudcoil.models.keda`, use the package's typed lookup to
select an exact Kubernetes kind and API version:

```python
from cloudcoil.models.keda import get_model

ScaledObject = get_model("ScaledObject", api_version="keda.sh/v1alpha1")

for resource in ScaledObject.list(namespace="default"):
    print(resource.name)
```

The lookup is local; `list` reads the configured cluster. Async code uses
`await ScaledObject.async_list(namespace="default")`. Direct class imports are also supported; the
lookup avoids depending on schema-derived module names.

Install the upstream KEDA CRDs and operator separately before making API calls.
The model package supplies Python types and client methods, not the operator.

Use the shared [resource guide](https://cloudcoil.github.io/cloudcoil/resources/)
for constructors, builders, writes and watches, and the
[controller guide](https://cloudcoil.github.io/cloudcoil/controllers/) for
reconciliation. Pydantic validates constructed models at runtime; generated
annotations provide field completion and static type checking.

### Maintain this integration

From the Cloudcoil repository root:

```sh
make gen-repo-keda
make -C output/models-keda lint test check-artifacts
```

Rendering generates the models before validation. The
[model release guide](https://cloudcoil.github.io/cloudcoil/model-releases/)
covers source updates, artifact checks and publishing.

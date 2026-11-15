# GraphQL WebSocket implementation (vendored)

This directory vendors the `channels_graphql_ws` Python package exactly as
published in the `baseapp-django-channels-graphql-ws` 1.0.0rc9 wheel on PyPI.
That distribution is a release of DjangoChannelsGraphqlWs
(https://github.com/datadvance/DjangoChannelsGraphqlWs), by Alexander A.
Prokhorov / DATADVANCE, under the MIT license.

- The eight `.py` modules and `LICENSE` match, byte for byte, the SHA-256
  entries of the wheel's `RECORD` (checked on 2026-11-15 against the copy
  installed in the image of the current production base, 89759125).
- The original copyright notices remain in every module; `LICENSE` is the
  wheel's own license file.
- Earlier notes referred to `silverlogic/DjangoChannelsGraphqlWs` at commit
  `b34ef1aae9a5b16683dc61d0488055502787ec84` as the source of that release;
  that reference was not re-verified offline.

Why it is vendored: the published package pins `graphql-core==3.2.3`, which is
affected by GHSA-vj8h-fx38-h3vc and GHSA-r77w-qph3-7vf8 (fixed in 3.2.12).
Shipping the unchanged source here lets the `graphql` extra require
`graphql-core >= 3.2.14, < 3.3`.

Rules for this directory:

- Do not edit the modules. Any update must replace them with another published
  release, re-check the hashes against that release's `RECORD`, keep `LICENSE`
  and the notices, and re-run the WebSocket subscription tests.
- Linters skip this directory (`.flake8`, `[tool.black]`, `[tool.isort]` in
  `pyproject.toml`), so the source stays identical to the upstream release.

Re-check, from the repository root, in an environment where the wheel is
installed:

```python
import base64, hashlib, importlib.metadata as md, pathlib

dist = md.distribution("baseapp-django-channels-graphql-ws")
here = pathlib.Path("channels_graphql_ws")
for f in dist.files:
    if f.hash and (f.parts[0] == "channels_graphql_ws" or f.name == "LICENSE"):
        local = here / f.name
        digest = base64.urlsafe_b64encode(hashlib.sha256(local.read_bytes()).digest())
        print(f.name, digest.rstrip(b"=").decode() == f.hash.value)
```

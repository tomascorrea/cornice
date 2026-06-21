# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from importlib.metadata import version


MARSHMALLOW_V4 = int(version("marshmallow").split(".")[0]) >= 4

# EXCLUDE moved from marshmallow.utils to marshmallow in v4
if MARSHMALLOW_V4:  # pragma: no cover
    from marshmallow import EXCLUDE  # noqa: F401
else:  # pragma: no cover
    from marshmallow.utils import EXCLUDE  # noqa: F401


def set_schema_context(schema, key, value):
    """Set context on schema. Uses Schema.context on v3, no-op on v4."""
    if not MARSHMALLOW_V4:  # pragma: no cover
        schema.context.setdefault(key, value)

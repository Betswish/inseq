# type: ignore[attr-defined]
"""Attribution methods for sequence-to-sequence transformer models 🔍"""

import sys
from importlib import metadata as importlib_metadata

from .models import AttributionModel, load


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()

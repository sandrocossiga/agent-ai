"""Top-level package for the agent library.

This package exposes the core functionality of the agent as well as
schemas and utilities. The design is intentionally simple and modular
to make it easy to extend with additional tools and functionality.
"""

from .core import Agent  # noqa: F401
from .schemas import AgentInput, AgentOutput  # noqa: F401
from .guard import sanitize  # noqa: F401

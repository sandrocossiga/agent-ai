"""Pydantic schemas for agent input and output.

The `AgentInput` model represents the structure of messages coming
into the agent. It currently contains a single `prompt` field but
can be extended to include additional metadata such as user IDs or
context objects.

The `AgentOutput` model defines the structure of the agent's
responses.
"""
from __future__ import annotations

from pydantic import BaseModel, Field


class AgentInput(BaseModel):
    """Structure for incoming agent requests."""

    prompt: str = Field(..., description="The raw user input to process.")


class AgentOutput(BaseModel):
    """Structure for outgoing agent responses."""

    answer: str = Field(..., description="The agent's computed answer.")

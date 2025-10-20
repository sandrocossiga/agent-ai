"""Core logic for the agent.

This module defines a simple `Agent` class that takes user input,
sanitizes it, validates it against a Pydantic model, and produces
a plan. The plan here is just a stub function that echoes the
input back as a list of tasks. In a real system, this would be
replaced by logic that calls an LLM or other planner component.
"""
from __future__ import annotations

from typing import List

from .schemas import AgentInput, AgentOutput
from .guard import sanitize


class Agent:
    """A simple agent that plans a response given user input."""

    def __init__(self) -> None:
        # In a more advanced implementation, dependencies such as
        # tool registries or LLM clients would be injected here.
        pass

    def plan(self, user_input: str) -> List[str]:
        """Generate a list of tasks based on the user input.

        The current implementation merely splits the sanitized input
        into words and prefixes each with "Task". A real planner
        would interpret the input and decide which tools to call.

        Args:
            user_input: Raw user input string.

        Returns:
            A list of task descriptions.
        """
        clean_input = sanitize(user_input)
        if not clean_input:
            return []
        words = clean_input.split()
        return [f"Task: {word}" for word in words]

    def run(self, data: AgentInput) -> AgentOutput:
        """Run the agent on structured input data.

        This method sanitizes the input, generates a plan, and
        returns an `AgentOutput` model. In a real implementation,
        this would likely execute the plan using tool calls.

        Args:
            data: An instance of `AgentInput` containing the
                user's prompt and any metadata.

        Returns:
            An `AgentOutput` containing the computed result.
        """
        tasks = self.plan(data.prompt)
        result = "; ".join(tasks) if tasks else "No tasks generated."
        return AgentOutput(answer=result)



def main() -> None:
    """Entry point for running the agent from the command line."""
    import argparse
    parser = argparse.ArgumentParser(description="Run the simple agent.")
    parser.add_argument("prompt", help="User prompt to process")
    args = parser.parse_args()
    agent = Agent()
    inp = AgentInput(prompt=args.prompt)
    out = agent.run(inp)
    print(out.answer)


if __name__ == "__main__":
    main()

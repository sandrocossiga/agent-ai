# Agent AI Project

This repository contains a modular Python agent designed to serve as a foundation for building more complex agentic systems. The project uses **Pydantic** for data validation, includes a basic input sanitization layer, and comes with a simple planner stub. It also includes an example adversarial test suite to help you develop with security in mind.

## Structure

- `src/agent/`
  - `core.py` – main agent logic and simple planner stub.
  - `schemas.py` – Pydantic models defining the inputs and outputs for the agent.
  - `guard.py` – utilities for sanitizing inputs to guard against prompt injection or other unsafe content.
  - `tools/` – directory intended for tool integrations (currently empty with a placeholder). Each tool should live in its own module.

- `tests/`
  - `test_production_security.py` – adversarial tests focused on security aspects like input sanitization.
  - `test_planner.py` – tests for the planner stub implementation.

- `.github/workflows/ci.yml` – GitHub Actions workflow for linting and running tests.

## Getting Started

Install dependencies (ideally within a virtual environment):

```bash
pip install -r requirements.txt
```

Run tests with `pytest`:

```bash
pytest -q
```

You can run the simple example planner directly:

```bash
python -m src.agent.core
```

## Security Considerations

The `guard.sanitize` function is designed to remove potentially harmful content from user inputs. It is deliberately simple and should be extended to suit your specific threat model. The adversarial tests in `test_production_security.py` can serve as a starting point for thinking about security and robustness.

## Contributing

Contributions are welcome! Please open an issue or pull request to discuss improvements, additional tools, or more extensive testing.

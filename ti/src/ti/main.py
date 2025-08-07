#!/usr/bin/env python
import warnings

from ti.crew import Ti

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {"topic": "<OpenAI agents>"}

    try:
        Ti().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

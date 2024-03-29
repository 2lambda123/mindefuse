#! usr/bin/env python3.7


class EngineConfig:
    """
    Configuration of the Evaluation Engine
    """

    """File to where the evaluation results will be registered"""
    OUTPUT_FILE = "./evaluation/output/results.csv"

    """Mode in which the file is opened"""
    EDIT_MODE = "a+"

    """Arguments used for tests"""
    TEST_FIELDS = ["rounds", "secret", "algorithm"]

    """Identifiers of the CSV file attributes"""
    FIELD_NAMES = [
        "algorithm",
        "secret",
        "type",
        "size",
        "solved",
        "rounds",
        "time",
    ]

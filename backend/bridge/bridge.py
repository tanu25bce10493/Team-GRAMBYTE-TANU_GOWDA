import subprocess
import json
import os
from typing import Dict, Any


def run_cpp_engine(resource_id: str, start_time: str, end_time: str) -> Dict[str, Any]:
    """
    Executes the C++ scheduling engine and returns its response.
    """

    cpp_engine_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "cpp",
        "graph_engine.exe"
    )

    if not os.path.exists(cpp_engine_path):
            return {
                "status": 500,
                "message": "C++ engine executable not found."
            }
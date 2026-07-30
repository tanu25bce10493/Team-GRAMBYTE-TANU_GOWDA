import subprocess
import json
import os
from typing import Dict, Any

from .logger import log_booking


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

    try:
        # Execute the C++ engine
        result = subprocess.run(
            [
                cpp_engine_path,
                resource_id,
                start_time,
                end_time
            ],
            capture_output=True,
            text=True,
            timeout=1
        )

        # Convert JSON output from C++ into a Python dictionary
        response = json.loads(result.stdout)

        # Log only successful bookings
        if response.get("status") == 200:
            log_booking({
                "resource_id": resource_id,
                "start_time": start_time,
                "end_time": end_time
            })

        return response

    except subprocess.TimeoutExpired:
        return {
            "status": 504,
            "message": "C++ engine execution timed out."
        }

    except json.JSONDecodeError:
        return {
            "status": 500,
            "message": "Invalid JSON returned by C++ engine."
        }

    except Exception as e:
        return {
            "status": 500,
            "message": str(e)
        }
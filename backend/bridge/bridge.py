import subprocess
import json
import os
from typing import Dict, Any

from .logger import log_booking


def run_cpp_engine(resource_id: str, start_time: str, end_time: str) -> Dict[str, Any]:
    """
    Executes the C++ scheduling engine and returns its response.
    """

    cpp_engine_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "cpp",
            "build",
            "SyncReserveAI.exe"
        )
    )

    if not os.path.exists(cpp_engine_path):
        return {
            "success": False,
            "status": 500,
            "message": f"C++ engine executable not found: {cpp_engine_path}"
        }

    try:

        result = subprocess.run(
            [
                cpp_engine_path,
                resource_id,
                start_time,
                end_time
            ],
            capture_output=True,
            text=True,
            timeout=3
        )

        if result.returncode != 0:
            return {
                "success": False,
                "status": 500,
                "message": result.stderr.strip() or "C++ engine failed."
            }

        response = json.loads(result.stdout)

        if response.get("success"):

            log_booking({
                "resource_id": resource_id,
                "start_time": start_time,
                "end_time": end_time
            })

        return response

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "status": 504,
            "message": "C++ engine execution timed out."
        }

    except json.JSONDecodeError:
        return {
            "success": False,
            "status": 500,
            "message": "Invalid JSON returned by C++ engine."
        }

    except Exception as e:
        return {
            "success": False,
            "status": 500,
            "message": str(e)
        }
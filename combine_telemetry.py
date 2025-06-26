"""
Daikibo IIoT Telemetry Data Combiner
Author: Nitya
Description:
This script normalizes telemetry data from two types of IIoT devices:
- Device A: Sends data with ISO 8601 timestamp
- Device B: Sends data with epoch seconds timestamp
The output provides a unified format where all timestamps are converted to epoch milliseconds.
"""

from datetime import datetime
import json

def iso8601_to_epoch_ms(iso_str):
    """
    Convert ISO 8601 timestamp string to epoch milliseconds.
    """
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

def normalize_device_a(data):
    """
    Normalize Device A telemetry data.
    """
    return {
        "device_id": data.get("device_id"),
        "temperature": data.get("temperature"),
        "timestamp_ms": iso8601_to_epoch_ms(data.get("timestamp"))
    }

def normalize_device_b(data):
    """
    Normalize Device B telemetry data.
    """
    return {
        "device_id": data.get("device_id"),
        "pressure": data.get("pressure"),
        "timestamp_ms": int(data.get("timestamp")) * 1000
    }

def main():
    # Example telemetry data from Device A
    device_a_data = {
        "device_id": "A123",
        "temperature": 75,
        "timestamp": "2025-06-26T08:30:00Z"
    }

    # Example telemetry data from Device B
    device_b_data = {
        "device_id": "B456",
        "pressure": 30,
        "timestamp": 1751230200  # epoch seconds
    }

    # Normalize both data sources
    normalized_a = normalize_device_a(device_a_data)
    normalized_b = normalize_device_b(device_b_data)

    # Combine the data
    combined = [normalized_a, normalized_b]

    # Pretty print the combined output
    print(json.dumps(combined, indent=2))

if __name__ == "__main__":
    main()

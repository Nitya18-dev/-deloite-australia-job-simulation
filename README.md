# IIoT Telemetry Data Combiner

This project contains a Python script that helps **Daikibo Industrials** combine telemetry data from two types of IIoT devices:
- **Device A**: Sends telemetry data with ISO 8601 timestamp.
- **Device B**: Sends telemetry data with epoch seconds timestamp.

The script normalizes both data formats so that all telemetry has timestamps in **epoch milliseconds**, enabling unified analysis and reporting.

---

## 📂 Files
- `combine_telemetry.py` — The main Python script for data normalization.
- `README.md` — This documentation file.
- `sample_output.json` *(optional)* — Example of normalized combined output.

---

## 🚀 How to Run
### Requirements
- Python 3.x

### Steps
1️⃣ Clone this repository or download the files.  
2️⃣ Run the script using:
python combine_telemetry.py



---

## 📝 Example Output
```json
[
  {
    "device_id": "A123",
    "temperature": 75,
    "timestamp_ms": 1751230200000
  },
  {
    "device_id": "B456",
    "pressure": 30,
    "timestamp_ms": 1751230200000
  }
]
⚙ How it Works
✅ The script:

Converts ISO 8601 timestamps (from Device A) to epoch milliseconds.

Converts epoch seconds (from Device B) to epoch milliseconds.

Outputs combined data as JSON.

💡 Purpose
This solution enables Daikibo to:

Ingest and process telemetry data uniformly.

Simplify downstream analytics.

Support real-time and historical monitoring across devices.


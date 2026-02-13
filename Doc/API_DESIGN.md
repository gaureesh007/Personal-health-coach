Endpoints
Upload Medical History
POST /upload-history

Sync Wearable Data
POST /sync-wellness

Get Recommendation
POST /recommend


Response:
//json
{
  "risk_level": "Yellow",
  "summary": "...",
  "recommendations": [
    "Improve sleep hygiene",
    "Reduce sodium intake"
  ]
}

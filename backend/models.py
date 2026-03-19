from enum import Enum

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Severity(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"


class Patient(BaseModel):
    patient_id: str
    age: int
    gender: str
    baseline_summary: Optional[str] = None


class MedicalEvent(BaseModel):
    event_id: str
    patient_id: str
    condition: str
    severity: Severity
    timestamp: datetime
    structured_data: Optional[dict] = None


class WellnessLog(BaseModel):
    patient_id: str
    heart_rate: Optional[float] = None
    sleep_hours: Optional[float] = None
    stress_index: Optional[float] = None
    step_count: Optional[int] = None
    blood_pressure_systolic: Optional[float] = None
    blood_pressure_diastolic: Optional[float] = None
    timestamp: datetime


class RecommendRequest(BaseModel):
    patient_id: str
    query: str
    model: Optional[str] = Field(default="gpt-4o", description="LLM model to use")


class RecommendResponse(BaseModel):
    risk_level: str
    summary: str
    recommendations: list[str]
    confidence_score: float
    model_used: str


class LLMModel(BaseModel):
    id: str
    name: str
    provider: str
    description: str
    context_window: int
    cost_per_1k_tokens: float

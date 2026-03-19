from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import (
    Patient, MedicalEvent, WellnessLog,
    RecommendRequest, RecommendResponse, LLMModel
)

app = FastAPI(
    title="MedReduce AI - Personal Health Coach",
    description="Cost-Aware RAG-Based Health Monitoring & Recommendation System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Available LLM models
AVAILABLE_MODELS: list[LLMModel] = [
    LLMModel(
        id="gpt-4o",
        name="GPT-4o",
        provider="OpenAI",
        description="OpenAI's most capable multimodal model with large context window.",
        context_window=128000,
        cost_per_1k_tokens=0.005,
    ),
    LLMModel(
        id="gpt-4o-mini",
        name="GPT-4o Mini",
        provider="OpenAI",
        description="Affordable and fast OpenAI model for lightweight queries.",
        context_window=128000,
        cost_per_1k_tokens=0.00015,
    ),
    LLMModel(
        id="claude-3-5-sonnet",
        name="Claude 3.5 Sonnet",
        provider="Anthropic",
        description="Anthropic's high-performance model with strong reasoning capabilities.",
        context_window=200000,
        cost_per_1k_tokens=0.003,
    ),
    LLMModel(
        id="claude-3-haiku",
        name="Claude 3 Haiku",
        provider="Anthropic",
        description="Anthropic's fastest and most compact model for cost-effective inference.",
        context_window=200000,
        cost_per_1k_tokens=0.00025,
    ),
    LLMModel(
        id="llama-3-8b",
        name="Llama 3 8B",
        provider="Meta (Local)",
        description="Open-source local LLM for privacy-preserving on-device inference.",
        context_window=8192,
        cost_per_1k_tokens=0.0,
    ),
    LLMModel(
        id="llama-3-70b",
        name="Llama 3 70B",
        provider="Meta (Local)",
        description="Large open-source local model with strong medical reasoning.",
        context_window=8192,
        cost_per_1k_tokens=0.0,
    ),
    LLMModel(
        id="mistral-7b",
        name="Mistral 7B",
        provider="Mistral AI (Local)",
        description="Efficient open-source local model optimized for instruction following.",
        context_window=32768,
        cost_per_1k_tokens=0.0,
    ),
]


@app.get("/")
def root():
    return {"message": "MedReduce AI Health Coach API is running"}


@app.get("/models", response_model=list[LLMModel])
def list_models():
    """Return all available LLM models."""
    return AVAILABLE_MODELS


@app.get("/models/{model_id}", response_model=LLMModel)
def get_model(model_id: str):
    """Return details for a specific LLM model."""
    for model in AVAILABLE_MODELS:
        if model.id == model_id:
            return model
    raise HTTPException(status_code=404, detail=f"Model '{model_id}' not found")


@app.post("/recommend", response_model=RecommendResponse)
def recommend(request: RecommendRequest):
    """Generate a health recommendation (stub – wire up RAG pipeline here)."""
    # Validate model
    valid_ids = {m.id for m in AVAILABLE_MODELS}
    if request.model not in valid_ids:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown model '{request.model}'. Valid options: {sorted(valid_ids)}"
        )

    # Stub response – replace with real RAG + LLM call
    return RecommendResponse(
        risk_level="Yellow",
        summary="Preliminary assessment based on available data.",
        recommendations=[
            "Maintain regular physical activity.",
            "Monitor blood pressure weekly.",
            "Ensure 7-8 hours of sleep per night.",
        ],
        confidence_score=0.75,
        model_used=request.model,
    )

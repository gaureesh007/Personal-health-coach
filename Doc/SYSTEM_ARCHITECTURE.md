User → API → Preprocessor → Embedding Model
                          ↓
                    Vector Database
                          ↓
                    Retrieval Layer
                          ↓
             Context Compression Engine
                          ↓
                    LLM Recommendation Engine
                          ↓
                        Output

                        Architecture Layers
1. Data Ingestion Layer

EHR upload

Wearable sync (heart rate, sleep, steps)

Lab report parser (PDF → structured JSON)

2. Embedding Layer

Convert medical chunks to embeddings

Store in vector DB

3. Retrieval Layer

Retrieve only relevant historical events

Filter by time relevance + severity

4. Compression Layer (Critical for cost)

Summarize long-term history

Keep acute conditions full

Archive old low-risk events

5. Recommendation Engine

Risk detection

Lifestyle advice

Alert system

Techniques Used
1. Smaller Embedding Model

Use:

text-embedding-3-small
or

open-source MiniLM

2. Smaller LLM for Preprocessing

Use lightweight LLM for:

Summaries

Cleaning

Reserve larger model for:

Critical medical reasoning

3. Cache Layer

If:
User asks same question twice
→ Return cached answer

4. Token Budgeting

Set:

Max context tokens = 2000
Max completion tokens = 500

5. Batch Embeddings

Batch process reports to reduce API calls.

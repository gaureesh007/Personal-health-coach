Why Compression?

Medical history grows exponentially.
Sending everything to LLM = $$$

Compression Strategy
1. Hierarchical Memory
Tier 1: Active Conditions (Full Detail)
Tier 2: Recent 6 Months (Partial Detail)
Tier 3: Older Data (Summarized)

2. Periodic Summarization

Every 30 days:

Summarize old logs

Convert into high-level summary

Store summary as new vector

Archive raw logs

3. Delta Updates

Only send:

What changed

What deviated from baseline

Instead of sending:

Entire medical record

4. Example

Instead of:

"Patient BP 140/90, 142/92, 145/95 over 3 weeks..."

Compress to:

"Sustained elevated BP trend over 3 weeks with upward progression."

Token cost reduced by ~70%

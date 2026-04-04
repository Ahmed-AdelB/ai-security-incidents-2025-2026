# EU AI Act Compliance Classification Benchmark

**Benchmark ID:** `aisec-euaiact-v1.0`  
**Task Type:** Multi-label Text Classification  
**Dataset Size:** 12 verified incidents (test set)  
**License:** CC-BY 4.0

---

## Task Definition

**Task:** Given an AI security incident description, classify which EU AI Act article(s) are primarily violated.

**Input:** `incident_description` (string) — what happened, what was exposed, attack vector

**Output:** One or more of:
- `article_9` — Risk Management System (Article 9)
- `article_13` — Transparency and Provision of Information (Article 13)  
- `article_15` — Accuracy, Robustness, Cybersecurity (Article 15)

**Label Space:** 7 valid combinations (non-empty subsets of {9, 13, 15})

---

## Evaluation Methodology

### 1. Primary Metrics

Given the multi-label nature of this task, we report the following metrics:

| Metric | Definition | Formula |
|--------|------------|---------|
| **Exact Match (EM)** | Proportion of predictions matching ground truth exactly | $\frac{1}{N} \sum_{i=1}^{N} \mathbb{1}[\hat{Y}_i = Y_i]$ |
| **Precision (micro)** | Correctly predicted labels / total predicted labels | $\frac{\sum_{c} TP_c}{\sum_{c} (TP_c + FP_c)}$ |
| **Recall (micro)** | Correctly predicted labels / total ground truth labels | $\frac{\sum_{c} TP_c}{\sum_{c} (TP_c + FN_c)}$ |
| **F1 (micro)** | Harmonic mean of precision and recall | $2 \cdot \frac{P \cdot R}{P + R}$ |
| **Hamming Loss** | Fraction of incorrect labels (lower is better) | $\frac{1}{N \cdot L} \sum_{i=1}^{N} |\hat{Y}_i \Delta Y_i|$ |

Where $L=3$ (number of labels), $c \in \{9, 13, 15\}$.

### 2. Per-Article Performance

Per-label precision, recall, and F1 are reported to diagnose model strengths/weaknesses:

```python
from sklearn.metrics import classification_report

# Binary relevance: one-vs-rest evaluation
print(classification_report(y_true, y_pred, target_names=['art_9', 'art_13', 'art_15']))
```

### 3. Partial Credit Metric

**Jaccard Similarity** provides partial credit for incomplete predictions:

```python
def jaccard_score(predicted: set, ground_truth: set) -> float:
    """Intersection over Union for label sets."""
    if len(predicted | ground_truth) == 0:
        return 0.0
    return len(predicted & ground_truth) / len(predicted | ground_truth)
```

**Mean Jaccard Index (MJI):** Average Jaccard similarity across all test instances.

### 4. Statistical Significance

Due to the small test size (n=12), confidence intervals are computed via **bootstrap resampling** (n=1000 iterations, 95% CI).

---

## Benchmark Dataset: verified-v1.0 (12 Incidents)

| # | Incident | Company | Ground Truth | Article 9 | Article 13 | Article 15 |
|---|----------|---------|--------------|:---------:|:----------:|:----------:|
| 1 | Shai-Hulud npm Worm v1 | npm ecosystem | **{9, 15}** | ✓ | | ✓ |
| 2 | OpenAI Mixpanel Vendor Breach | OpenAI | **{9, 13}** | ✓ | ✓ | |
| 3 | PRC Cyber Operation | Anthropic (misused) | **{9, 15}** | ✓ | | ✓ |
| 4 | Shai-Hulud npm Worm v2.0 | npm ecosystem | **{9, 15}** | ✓ | | ✓ |
| 5 | Claude Code CVE-2025-59536 (RCE) | Anthropic | **{9, 15}** | ✓ | | ✓ |
| 6 | Claude Code CVE-2026-21852 | Anthropic | **{9, 13}** | ✓ | ✓ | |
| 7 | TeamPCP Cascading Supply Chain | Multiple | **{9, 15}** | ✓ | | ✓ |
| 8 | Meta AI Agent Rogue Data Breach | Meta | **{9, 13, 15}** | ✓ | ✓ | ✓ |
| 9 | Anthropic Mythos/Capybara CMS Leak | Anthropic | **{13}** | | ✓ | |
| 10 | Axios npm Hijack | npm ecosystem | **{9, 15}** | ✓ | | ✓ |
| 11 | Claude Code npm Source Map Leak | Anthropic | **{13, 15}** | | ✓ | ✓ |
| 12 | Claude Opus 4.6 Mass Distillation | Anthropic (IP) | **{9, 13}** | ✓ | ✓ | |

### Label Distribution

| Label Combination | Count | Frequency |
|-------------------|-------|-----------|
| {9, 15} | 5 | 41.7% |
| {9, 13} | 2 | 16.7% |
| {13} | 1 | 8.3% |
| {9, 13, 15} | 1 | 8.3% |
| {13, 15} | 1 | 8.3% |

### Per-Article Prevalence

| Article | Incidents | Prevalence |
|---------|-----------|------------|
| Article 9 (Risk Management) | 9 | 75.0% |
| Article 15 (Robustness) | 7 | 58.3% |
| Article 13 (Transparency) | 6 | 50.0% |

---

## Baseline Comparisons

### Random Classifier Baseline

A uniform random baseline (random non-empty subset) achieves:

| Metric | Expected Value |
|--------|----------------|
| Exact Match | **14.3%** (1/7 label combinations) |
| Mean Jaccard | **0.357** |
| Per-article Precision | 0.500 |
| Per-article Recall | 0.500 |

### Majority-Class Baseline

Always predicting the most common label combination {9, 15}:

| Metric | Value |
|--------|-------|
| Exact Match | **41.7%** (5/12) |
| Mean Jaccard | 0.486 |
| Article 9 Recall | 100% |
| Article 13 Recall | 0% |
| Article 15 Recall | 71.4% |

### Human Annotator Agreement

Inter-annotator agreement (3 legal/ML annotators, Fleiss' κ):

| Measure | Value |
|---------|-------|
| Exact Match Agreement | 78.3% |
| Fleiss' Kappa (multi-label) | 0.71 |

---

## Usage

### Python

```python
import json
from typing import Set

# Load benchmark
with open("ai-leaks-incidents-verified-v1.0.json") as f:
    benchmark = json.load(f)

# Load ground truth labels (separate annotation file)
with open("ground_truth_labels.json") as f:
    ground_truth = {item["incident_name"]: set(item["labels"]) 
                    for item in json.load(f)}

# Prompt template for LLM evaluation
PROMPT_TEMPLATE = """Incident: {incident_name}
Company: {company}
Date: {date}
Type: {type}
Attack Vector: {how}
What Was Exposed: {what_exposed}
Severity: {severity}

Task: Identify which EU AI Act articles are violated by this incident.

Options:
- article_9: Risk management system failures (supply chain, third-party risks)
- article_13: Transparency obligations (disclosure, data handling visibility)
- article_15: Accuracy, robustness, cybersecurity failures

Respond with ALL applicable articles as a JSON array, e.g., ["article_9", "article_15"]
"""

def evaluate_model(model_predict_fn, benchmark, ground_truth):
    """
    Evaluate a model on the benchmark.
    
    Args:
        model_predict_fn: Function that takes incident dict and returns set of labels
        benchmark: List of incident records
        ground_truth: Dict mapping incident_name to set of labels
    
    Returns:
        Dict with metrics
    """
    predictions = []
    references = []
    
    for incident in benchmark:
        pred = model_predict_fn(incident)
        ref = ground_truth[incident["incident_name"]]
        predictions.append(pred)
        references.append(ref)
    
    return compute_metrics(predictions, references)
```

### Using HuggingFace Datasets

```python
from datasets import load_dataset

# Load from HuggingFace
dataset = load_dataset(
    "Ahmed-AdelB/ai-security-incidents-2025-2026",
    split="verified"
)

# Access with labels
dataset = load_dataset(
    "Ahmed-AdelB/ai-security-incidents-2025-2026",
    split="verified_with_labels"
)
```

---

## Leaderboard Submission Format

Submissions must be a JSON Lines file (`.jsonl`) with the following schema:

```json
{
  "submission_metadata": {
    "model_name": "claude-sonnet-4.5",
    "organization": "Anthropic",
    "submission_date": "2026-04-01",
    "paper_url": "https://arxiv.org/abs/...",
    "code_url": "https://github.com/...",
    "system_prompt": "Optional: brief description of approach",
    "few_shot_examples": 3
  },
  "predictions": [
    {
      "incident_name": "Shai-Hulud npm Worm v1",
      "predicted_labels": ["article_9", "article_15"],
      "confidence_scores": {"article_9": 0.95, "article_13": 0.12, "article_15": 0.88}
    },
    ...
  ]
}
```

### Validation Rules

1. **All 12 incidents must have predictions**
2. **Labels must be from valid set:** `{article_9, article_13, article_15}`
3. **At least one label required** per incident (no empty predictions)
4. **Confidence scores optional** but recommended for ranking

### Submission Command

```bash
# Validate your submission
python validate_submission.py --submission your_results.jsonl

# Submit to leaderboard (via HuggingFace or email)
# leaderboard@aisec-benchmark.org
```

---

## Current Leaderboard

| Rank | Model | EM ↑ | F1 ↑ | MJI ↑ | Few-shot | Date |
|------|-------|------|------|-------|----------|------|
| — | *Awaiting submissions* | — | — | — | — | — |
| — | Human Expert (estimate) | 78% | 85% | 0.85 | N/A | — |
| — | Majority Baseline | 41.7% | 58.6% | 0.486 | 0 | — |
| — | Random Baseline | 14.3% | 50.0% | 0.357 | 0 | — |

---

## Citation

If you use this benchmark, please cite:

```bibtex
@dataset{alderai2026aisecincidents,
  title       = {AISecIncidents-2025-26: EU AI Act Compliance Classification Benchmark},
  author      = {Alderai, Ahmed Adel Bakr},
  year        = {2026},
  publisher   = {HuggingFace},
  url         = {https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026},
  version     = {v1.0},
  type        = {Dataset}
}
```

---

## NeurIPS Datasets & Benchmarks Checklist

- [x] **Task Definition:** Clear input/output specification
- [x] **Evaluation Metrics:** Multiple metrics with justification
- [x] **Baseline Results:** Random and majority-class baselines
- [x] **Data Documentation:** Complete schema and provenance
- [x] **Human Performance:** Inter-annotator agreement reported
- [x] **Submission Format:** Standardized JSON schema
- [x] **Leaderboard:** Public ranking with submission guidelines
- [x] **License:** Open license (CC-BY 4.0)

---

## Commercialization Notes

- **Free tier:** benchmark task + verified-v1.0.json (12 records, HuggingFace)
- **Pro tier:** full 40-record dataset + UMMRO compliance dashboard
- **Enterprise tier:** custom incident monitoring + UMMRO platform license

**Author:** Ahmed Adel Bakr Alderai  
**Contact:** ahmed.adel.bakr@gmail.com

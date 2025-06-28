# T<sup>5</sup>Score
An implementation of the T<sup>5</sup>Score evaluation metric for assessing the quality of LLM-generated topic sets. Topic sets are natural language one sentence summary of a main theme that recurs in a given collection of documents.

## 📦 How to install

```cmd
pip install tpower5score
```

## 🚀 How to use

```python
    import tpower5score

    topics_set = [<topics_set>]
    docs = [<documents>]

    agg_weights = {
        'Interpretability': 0.2,
        'Topic Coverage': 0.2,
        'Document Coverage': 0.2,
        'Overlap': 0.2,
        'Rank': 0.2
    }

    aspects, agg_score = tpower5score.evaluate(topics_set, docs)
```

Or see working example in [examples/main.py]()

## 📖 Citation

If you use this package in your work, please cite:

```bibtex
@inproceedings{trainin-abend-2025-t5,
  title={$T^5Score$: A Methodology for Automatically Assessing the Quality of LLM Generated Multi-Document Topic Sets},
  author={Trainin Itamar, Omri Abend},
  booktitle = "Findings of the Association for Computational Linguistics: ACL 2025",
  year = "2025",
}

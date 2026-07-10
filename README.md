# genpark-product-spec-extractor-skill

This repository contains the **GenPark Product Spec Extractor Skill** — an agent configuration skill config (`skill.json`), a production-ready Python SDK client (`spec_extractor.py`), and executable verification tests. It is designed to scan messy HTML segments or unstructured text descriptions to parse, isolate, and return key technical specifications.

---

## 🚀 Capabilities

* **HTML Filter Rules:** Automatically strips tag components to normalize plain text structures.
* **Regex Pattern Scanners:** Matches standard descriptor layouts (e.g. Dimensions, Material, Colors, Weight).
* **Metadata Normalizations:** Emits clean key-value maps ready for ingestion into database storage.

---

## 🛠️ Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 SDK Usage Reference

```python
from spec_extractor import ProductSpecExtractorClient

client = ProductSpecExtractorClient()

result = client.extract_specs("Color: Slate Black\nMaterial: Wood")
print(result["extracted_specifications"])
```

---

## 📜 License
This project is licensed under the MIT License.

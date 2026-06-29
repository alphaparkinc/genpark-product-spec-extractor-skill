import os
import re
from typing import Dict, Any, Optional

class ProductSpecExtractorClient:
    """
    Production-grade feature extraction utility. Parses unstructured text and HTML
    for technical specifications, returning normalized metadata maps.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("EXTRACTOR_API_KEY")

    def extract_specs(self, text: str) -> Dict[str, Any]:
        """
        Parses input string for standard e-commerce specification labels.
        """
        clean_text = re.sub(r'<[^>]+>', '\n', text) # strip html tags
        lines = clean_text.split('\n')
        
        specs = {}
        target_keys = ["dimensions", "weight", "material", "color", "battery", "warranty"]

        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Match standard "Key: Value" or "Key - Value" patterns
            match = re.match(r'^([^:-]+)\s*[:|-]\s*(.+)$', line)
            if match:
                key = match.group(1).strip().lower()
                val = match.group(2).strip()
                
                # Check if it fits our target e-commerce attributes
                for tk in target_keys:
                    if tk in key:
                        specs[tk] = val

        return {
            "extracted_specifications": specs
        }

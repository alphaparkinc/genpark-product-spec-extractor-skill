import sys
import json
from spec_extractor import ProductSpecExtractorClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== GenPark Product Spec Extractor Verification ===")
    client = ProductSpecExtractorClient()

    # Raw messy HTML description from website
    raw_input = (
        "<div>\n"
        "  <h1>Super Hub speaker</h1>\n"
        "  <p>Best audio experience in 2026</p>\n"
        "  <ul>\n"
        "    <li>Dimensions: 10 x 5 x 5 inches</li>\n"
        "    <li>Weight: 24 ounces</li>\n"
        "    <li>Material - Aluminum housing</li>\n"
        "    <li>Color: Slate Black</li>\n"
        "    <li>Warranty - 3 Years Manufacturer</li>\n"
        "  </ul>\n"
        "</div>"
    )

    result = client.extract_specs(raw_input)
    print("\n--- Extracted Spec Metadata Map ---")
    print(json.dumps(result["extracted_specifications"], indent=2))

if __name__ == "__main__":
    main()

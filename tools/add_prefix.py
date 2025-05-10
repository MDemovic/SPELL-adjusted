from pathlib import Path
import re

file_name = "dataset_1_1000.owl"
base_uri = "https://orbis-security.com/pe-malware-ontology#"

path = Path(file_name)
text = path.read_text(encoding="utf-8")

updated = re.sub(r'rdf:about="#([^"]+)"',
                 rf'rdf:about="{base_uri}\1"',
                 text)

path.write_text(updated, encoding="utf-8")
print(f"Prefixes added to: {file_name}")

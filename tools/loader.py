import json
px = "https://orbis-security.com/pe-malware-ontology#"

with open("dataset_x_y_examples.json", "r") as f:
    data = json.load(f)

# positive examples
with open("pos.txt", "w") as pos:
    for pos_example in data["positive"]:
        id = pos_example.split(":", 1)[1]
        iri = px + id
        pos.write(iri + "\n")

# negative examples
with open("neg.txt", "w") as neg:
    for neg_example in data["negative"]:
        id = neg_example.split(":", 1)[1]
        iri = px + id
        neg.write(iri + "\n")
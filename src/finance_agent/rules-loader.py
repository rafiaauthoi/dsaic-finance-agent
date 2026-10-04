# Pre-reqs
import yaml
from collections import Counter

# Import yaml
with open("docs\\wsa-guidelines\\wsa-club-finance-rules.yaml", "r") as yaml_file:
    content = yaml.safe_load(yaml_file)

rules = content["rules_index"]

# Count and display rules
counts = Counter()

for rule in rules:
    category = rule["id"].split("-")[0]
    counts[category] += 1

print(f"Loaded {len(rules)} rules from docs/wsa-guidelines/wsa-club-finance-rules.yaml")
print(f"Event: {counts['EVT']} rules")
print(f"Operational: {counts['OPS']} rules")
print(f"Conference: {counts['CNF']} rules")
print(f"Collaboration: {counts['COL']} rules")

# Extra
main_cat = {"EVT", "OPS", "CNF", "COL"}

print("\nOther Categories:")
for category, count in counts.items():
    if category not in main_cat:
        print(f"Found {count} rules in category {category}")
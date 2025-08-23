import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Dummy monitoring: comparing two sets of queries
ref_data = pd.DataFrame({"query": ["refund policy", "pricing", "support"]})
cur_data = pd.DataFrame({"query": ["refund policy", "new product", "discount"]})

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref_data, current_data=cur_data)

report.save_html("data/processed/drift_report.html")
print("Drift report generated at data/processed/drift_report.html")

install:
	pip install -r requirements.txt

ingest:
	python -m src.ingest --input data/raw --out data/processed

run:
	python -m src.serve --query "What is in our docs?"

drift:
	python monitoring/drift_monitor.py --baseline monitoring/baseline_stats.json

smoke:
	pytest -q

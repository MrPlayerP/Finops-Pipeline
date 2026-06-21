#This script isolates infrastructure data. If simulating data for cost protection, generate anomalous spikes so your analytics system has real issues to detect later
import json, os, random
from datetime import datetime, timedelta
def generate_mock_billing_data(days=30):
	os.makedirs('data/raw', exist_ok=True)
	base_date = datetime.utcnow() - timedelta(days=days)
	services = ["EC2", "S3", "RDS", "Redshift", "Lambda"]
	for i in range(days):
		current_date = base_date + timedelta(days=i)
		date_str = current_date.strftime("%Y-%m-%d")
		records = []
		for service in services:
			cost = random.uniform(20.0, 150.0)
			if date_str == (datetime.utcnow() - timedelta(days=4)).strftime("%Y-%m-%d") and service == "Redshift":
				cost = 2450.00
			records.append({
				"run_date": date_str,
				"cloud_provider": "AWS",
				"service": service,
				"cost_usd": round(cost, 2),
				"region": "us-east-1",
				"environment": "production"
			})
		with open(f"data/raw/billing_{date_str}.json", "w") as f:
			json.dump(records, f, indent=4)
if __name__ == "__main__":
generate_mock_billing_data()
print("Extraction complete: Files in data/raw/")
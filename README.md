🚚 LogiMind: AI-Powered Logistics Optimizer for Santova
Overview
LogiMind is a modular AI application designed to optimize global logistics operations for Santova. It leverages predictive modeling, natural language processing, and geospatial intelligence to streamline shipment tracking, customs compliance, and route efficiency — all while maintaining POPIA-aligned audit trails.

🔧 Core Features
Module	Description
🧠 Predictive ETA	Uses XGBoost to estimate arrival times based on distance, cargo weight, and weather
📄 Customs Parser	NLP engine (spaCy) extracts key fields from unstructured customs documents
🗺️ Route Dashboard	Real-time map visualization using Azure Maps for route tracking and risk alerts
🔐 Audit Logging	POPIA-compliant event logging for transparency and traceability
🧪 Tech Stack
Backend: FastAPI

ML Model: XGBoost

NLP: spaCy

Database: PostgreSQL

Visualization: Azure Maps + HTML/JS

Logging: JSON-based audit trail

🚀 Getting Started
1. Clone the repo
bash
git clone https://github.com/MampotjeMabusela/Logistics-Optimizer.git
cd Logistics-Optimizer
2. Install dependencies
bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
3. Train the ETA model
bash
python train_eta_model.py
4. Run the API
bash
uvicorn main:app --reload
5. Open the dashboard
Launch dashboard.html in your browser and insert your Azure Maps key.

📦 API Endpoints
Endpoint	Method	Description
/predict_eta	POST	Returns estimated arrival time for a shipment
/parse_customs	POST	Extracts structured fields from customs document text
🛡️ Compliance & Security
All data events are logged in audit_log.json with timestamps and action metadata

Designed to align with POPIA and GDPR standards for cross-border data handling

Modular architecture allows for encryption and role-based access control

🧭 Future Enhancements
Real-time weather and traffic integration

Role-based user authentication

Deployment via Docker + Azure App Service

Advanced anomaly detection for shipment delays

🤝 Credits
Built by Mampotje Mabusela Inspired by Santova’s commitment to Innovation Through Intelligence

📊 **MTA Ridership Prediction**
**Overview**
This project predicts NYC subway ridership at any given time using historical datasets and machine learning models. The workflow demonstrates end‑to‑end data engineering and analytics: ETL → preprocessing → modeling → deployment → visualization.

🚀 **Features**
ETL in Python: Automated ingestion and cleaning of raw MTA ridership datasets using Pandas and custom scripts.

Preprocessing: Centralized feature engineering (dummy encoding, scaling, feature alignment) for reproducible predictions.

Machine Learning: Models trained with Scikit‑Learn (Random Forest, Gradient Boosting) to forecast ridership patterns.

Deployment: FastAPI service containerized with Docker, serving predictions via REST API.

Visualization: Power BI dashboards built on processed data for interactive KPI monitoring.

📂 **Project Structure**

MTA-Ridership/\
│── data/               # Sample datasets (large files excluded via .gitignore)    
│── src/                # ETL + preprocessing scripts, FastAPI app       
│── models/             # Trained ML models + saved feature columns           
│── BI/                 # Power BI reports             
│── Dockerfile          # Container setup                
│── requirements.txt    # Python dependencies          
│── README.md           # Project documentation                                   

⚙️ **Tech Stack**\
Languages: Python (Pandas, NumPy, Scikit‑Learn, Matplotlib, Seaborn)\

Data Engineering: ETL + preprocessing in Python scripts

Deployment: FastAPI + Docker

Visualization: Power BI

🔧 **How to Run**


Clone the repository:

**bash**
git clone [https://github.com/sonalworkasfl-us/MTA-Ridership.git](https://github.com/sonalworkasfl-us/MTA-Ridership.git)
cd MTA-Ridership

Install dependencies:
**bash**
pip install -r requirements.txt

Build and run the FastAPI service with Docker:
**bash**
docker build -t mta-ridership .
docker run -p 8000:8000 mta-ridership


Access the API at:
http://localhost:8000/docs


📊 **Future Enhancements**
-Integrate Airflow for orchestration of ETL jobs.

-Migrate storage to AWS Redshift/S3 for scalability.

-Add real‑time streaming ingestion from MTA feeds.

-Expand dashboards with anomaly detection and predictive alerts.

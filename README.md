Automated Currency Exchange ETL Pipeline and Dashboard
An end-to-end, production-ready data engineering project that automates the process of extracting foreign exchange rates, transforming raw data into structured models, storing them in a secure database, and serving them through an interactive web dashboard.

📌 Project Overview and Value Proposition
In modern data architectures, relying on manual data collection or brittle script execution leads to data loss and operational inefficiencies. This project replaces manual intervention with an automated, containerized, and orchestrated data factory.

What Happens If This Pipeline Didn't Exist?
No Automation (Airflow): Engineers would have to manually execute scripts daily. If a failure occurred overnight or during weekends, data gaps would form silently without logs or alerts.

No Isolation (Docker): Deploying the environment on a new machine would cause dependency hell, port conflicts, and OS-specific bugs.

No Persistence (PostgreSQL): Storing data in flat files (.csv/.txt) would become unmanageable as volume grows, making historical time-series queries incredibly slow and inefficient.

No Visualization (Streamlit): Business analysts would be forced to write raw SQL queries in pgAdmin to see currency trends, leading to a poor user experience.

🏗️ Architecture and Data Flow
The architecture is built on a multi-container Docker network, ensuring that the orchestration layer, database, and visualization layer communicate seamlessly.

Data Source: Frankfurter API (Returns raw EUR-based currency exchange data in JSON format).

Extract and Transform (Apache Airflow and Pandas): Python scripts fetch the raw data, clean metadata, handle data types, and prepare clean DataFrames.

Load (Psycopg2 and PostgreSQL): Cleaned data is appended into a relational PostgreSQL database container.

Visualization (Streamlit): A web application queries the live PostgreSQL database to generate dynamic time-series line charts based on user selection.

🛠️ Tech Stack
Core Language: Python 3.11+

Data Manipulation: Pandas

Orchestration: Apache Airflow 2.x

Containerization: Docker and Docker Compose

Database Management: PostgreSQL 15 and pgAdmin4

Web UI / Dashboard: Streamlit

🚀 How to Run the Project Locally
Follow these steps to spin up the entire multi-container infrastructure on your local machine.

Prerequisites
Docker and Docker Compose installed.

Python 3.11+ configured (with a virtual environment preferred).

1. Clone the Repository
Run the following commands in your terminal to clone and enter the project directory:

git clone https://github.com/kursadyavuzlu/Automated-Currency-Exchange-ETL-Pipeline-Dashboard.git

cd Automated-Currency-Exchange-ETL-Pipeline-Dashboard

2. Start the Multi-Container Infrastructure (Airflow and Postgres)
Run Docker Compose to build and start the database and orchestration layers by running this command in your terminal:

docker compose up -d

Access the Airflow UI at http://localhost:8080 to trigger or unpause the currency_etl_pipeline DAG.

Access pgAdmin4 at http://localhost:5050 to inspect the exchange_rates table under the postgres database.

3. Run the Streamlit Dashboard
Ensure your virtual environment is active, install the UI requirements, and launch the application using these commands:

pip install streamlit pandas psycopg2-binary

streamlit run dashboard.py

The interactive analytics dashboard will automatically open in your browser at http://localhost:8501.

📈 Future Roadmaps and Enhancements
Add Slack/Email notification alerts to the Airflow DAG on task failures.

Implement a dbt (Data Build Tool) layer for advanced data warehouse modeling and testing.

Migrate the local storage layer to a cloud-based warehouse (e.g., Snowflake or AWS Redshift).

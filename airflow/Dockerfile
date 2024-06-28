# Utiliser l'image officielle Airflow avec la version spécifique
FROM apache/airflow:2.9.2


# Copier les fichiers de script et les DAGs
#COPY ./dags /opt/airflow/dags

# Copier le fichier de dépendances et installer les packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


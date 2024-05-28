FROM apache/airflow:2.3.0-python3.8

# Switch to the non-root user
USER airflow

# Set the working directory to the home directory of the airflow user
WORKDIR /home/airflow

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./

# Configure Poetry to create a virtual environment in the project directory
RUN poetry config virtualenvs.in-project true

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy DAGs and Spark configuration
COPY dags/ /opt/airflow/dags/
COPY spark/spark-defaults.conf $SPARK_HOME/conf/

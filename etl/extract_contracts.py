
import os


from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PostgreSQL with PySpark") \
    .config("spark.jars", "./jars/postgresql-42.7.3.jar") \
    .getOrCreate()

url = "jdbc:postgresql://localhost:5432/midori"
properties = {
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "driver": "org.postgresql.Driver"
}

# Execute SQL query and load results into DataFrame
query = "(SELECT * FROM data_pipeline.fake_contracts ) AS temp_table"
df = spark.read.format("jdbc") \
    .option("url", url) \
    .option("dbtable", query) \
    .option("user", properties["user"]) \
    .option("password", properties["password"]) \
    .option("driver", properties["driver"]) \
    .load()

# Show the DataFrame
df.show()
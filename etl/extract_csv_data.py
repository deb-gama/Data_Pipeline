import sys

sys.path.append("/home/deb-gama/personal_projects/Data_Pipeline")

from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, lit, split

def spark_session():
    spark = SparkSession.builder.appName("Extract Clients").getOrCreate()
    return spark


def process_csv_extraction(config):
    
    csv_df = spark.read.option("delimiter", config["csv_delimiter"]).option("multiline",config["multiline_option"]).option("header", config["header_option"]).csv(config["csv_path_file"])

    if config.get("df_transformation_method"):
        transformed_df = config["df_transformation_method"](csv_df)
    else:
        transformed_df = csv_df
    
    transformed_df.show()



# total_null_count = transformed_clients_df.select([sum(col(c).isNull().cast("int")).alias(c) for c in transformed_clients_df.columns]).collect()[0]
# # # Row(Id=0, Nome=0, Endereço=0, Telefone=0, Email=0, CPF=0, Data de Nascimento=0)
# print(total_null_count)

if __name__ == '__main__':
    spark = spark_session()
    process_csv_extraction(clients_config)
    spark.stop()
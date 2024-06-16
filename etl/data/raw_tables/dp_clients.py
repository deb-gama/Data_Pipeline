def process_address_row(row):
    address = row["Endereço"]
    splitted_address = address.replace('\n', '/').split('/')
    client_id = row['Id']
    return (client_id, splitted_address[0], splitted_address[1], splitted_address[2].split(" ")[0], splitted_address[2].split(" ")[1], splitted_address[3])

def transform_clients_df(df):
    processed_rdd = df.rdd.map(lambda row: process_address_row(row))
    clients_df_processed = processed_rdd.toDF(["client_id", "address", "county", "postcode", "city", "state"])
    
    old_column_names = ["Id", "Nome", "Telefone", "Email", "CPF", "Data de Nascimento"]
    new_column_names = ["client_id", "name", "phone", "email", "document","birthdate"]

    for old_col, new_col in zip(old_column_names, new_column_names):
        df = df.withColumnRenamed(old_col, new_col)
    
    transformed_clients_df = df.drop('Endereço').join(clients_df_processed, df["client_id"] == clients_df_processed["client_id"]).withColumn("updated_at", lit(datetime.now())).drop(clients_df_processed.client_id)

    return transformed_clients_df

clients_config = {
    "csv_delimiter": ";",
    "multiline_option": True,
    "header_option": True,
    "csv_path_file": "data/fake_clients.csv",
    "df_name":  "clients_df",
    "df_transformation_method": transform_clients_df
}
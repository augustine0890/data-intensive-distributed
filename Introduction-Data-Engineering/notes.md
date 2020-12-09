# Data Engineering Introduction
**Data**
- Data is the new oil
    - Structured data: table (column and row), matrix, relational database
    - Semi-structured data: xml, csv, json
    - Unstructured data: e-mail, pdf, documents
    - Binary data: audio, video, image

**Data Engineer**
- Data mining: preprocessing, extracting some knowledge from data
- Big data: a lot of data (too much) - both structured and unstructed data
- Data pipeline: to flow from large amount of data to a pipeline that extracts data to a more useful form.
- __Data engineer__: creates a data pipeline where all the information that different sources. Transforming data from one format to another so that DS can pull data from different systems for analysis.
- Stream Data Source (Data Ingestion) --> Data Lake (Collection - Transformation) --> Data Warehouse (Processed)
- Kafka: Collecting data streams and putting into a data lake (Stream Source)
- Hadoop, Azure Data Lake, Amazon S3: Hold large amounts of data (Data Lake)
- Google BigQuery, Amazon Redshift, Amazon Athena: queries or analyze data (Data Warehouse)
- __DE__:
    - Build ETL pipeline
    - Build analysis tools
    - Maintain data warehouse and data lake

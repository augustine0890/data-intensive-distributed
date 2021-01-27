## Setting up Elasticsearch and Kibana
- Check Java Ver
    - `java -version`
- Download and Install `Elasticsearch` and `Kibana`
    - [Download Guide Elasticsearch](https://www.elastic.co/downloads/elasticsearch)
        - Run `curl http://localhost:9200/`
    - [Kibana](https://www.elastic.co/downloads/kibana)
        - Point your browser at `http://localhost:5601`
- Getting started with the [Elasticsearch](https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-elastic-stack.html)

## Elasticsearch
- Elasticsearch in Document Oriented
- Documents are JSON objects that are stored within an Elasticsearch Index. In the world of relational databases, documents can be compared to a row in table.
- Insert, delete, retrieve, analyze, __SEARCH__ documents
**Inverted Index**
- Maps words to the actual document locations of where they occur

## Indexing, Retrieving and Deleting Documents
- Relational DB <--> Elasticsearch: 
    - Table <--> Index
    - Row <--> Document
    - Column <--> Field
- Example Create Index API (`PUT`)
    ```json
    PUT /vehicles/_doc/123
    {
      "make": "Honda",
      "Color": "Black",
      "HP": 250,
      "milage": 24000,
      "price": 19300.97
    }
    ```
- Get (`GET`)
    ```json
    GET /vehicles/_doc/123/
    ```
- Update (`POST`)
    ```json
    POST /vehicles/_update/123/
    {
      "doc": {
        "price": 120000.23
      }
    }

    ```
- Delete (`DELETE`)
    ```json
    DELETE /vehicles/_doc/123
    ```
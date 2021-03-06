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

## Components of Index
- Example
    ```json
    PUT /business/_doc/110
    {
      "address": "57 New Dover Ln",
      "floors": 10,
      "offices": 21,
      "loc": {
        "lat": 40.707519,
        "lon": -74.008560
      }
    }

    PUT /employees/_doc/330
    {
      "name": "Richard Bell",
      "title": "Senior Accountant",
      "salary_usd": 115000.00,
      "hiredate": "Jan 19, 2015"
    }
    ```

## Distributed Execution of Requests
- Each Elasticsearch index is divided into shards. Shards are both logical and physical division of an index.
- Each Elasticsearch shard is a Lucene index
- The Lucene index is divided into smaller files called segments. A segment is a small Lucene index. Lucene searches in all segments sequentially.
- When you add new documents into your Elasticsearch index, Lucene creates a new segment and writies it.
- From time to time, Lucene merges smaller segments into a larger one. the merge can also be triggered manually from the Elasticsearch API.

Reference: [Operating Elasticsearch](https://fdv.github.io/running-elasticsearch-fun-profit/)

## Text Analysis for Indexing and Searching
- `ES --> Indexing <--> Analyzer (Tokenizer, Filter) --> Inverted Index --> Shards`

## Index Settings and Mappings
- `PUT /<target>/_settings`
    ```json
    PUT /customers/_settings
    {
      "index": {
        "routing.allocation.total_shards_per_node": 2,
        "number_of_replicas": 1
      }
    }
    ```
- `PUT /<target>/_mapping`
    ```json
    PUT /customers/_mapping
    {
        "properties": {
            "online": {
                "properties": {
                    "gender": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "age": {
                        "type": "integer"
                    },
                    "total_spent": {
                        "type": "float"
                    },
                    "is_new": {
                        "type": "boolean"
                    },
                    "name": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            }
        }
    }
    ```
    ```json
    PUT /customers/_doc/124
    {
      "name": "Mary Cranford",
      "address": "310 Clark Ave",
      "gender": "female",
      "age": 34,
      "total_spent": 550.75,
      "is_new": false
    }
    ```
- Create an index with settings and mapping
    
    ```json
    PUT /customers
    {
      "settings": {
        "number_of_replicas": 1,
        "number_of_shards": 2,
        "analysis": {},
        "refresh_interval": "1s"
      },
      "mappings": {
        "dynamic": false,
        "properties": {
          "online": {
            "properties": {
              "gender": {
                "type": "text",
                "analyzer": "standard"
              },
              "age": {
                "type": "integer"
              },
              "total_spent": {
                "type": "float"
              },
              "is_new": {
                "type": "boolean"
              },
              "name": {
                "type": "text",
                "analyzer": "standard"
              }
            }
          }
        }
      }
    }
    ```
- The analyzer
    ```json
    GET /_analyze
    {
      "analyzer" : "standard", // english
      "text" : "Quick Brown Foxes!"
    }
    ```

## Domain Specific Language (DSL)
- Search DSL components:
    - Query Context
    - Filter Context

- Example
    ```json
    GET /courses/_search
    {
      "query": {
        "match": {
          "name": "computer"
        }
      }
    }
    ```
    ```json
    GET /courses/_search
    {
      "query": {
        "exists": {
          "field": "professor.email" // "email"
        }
      }
    }
    ```
    ```json
    GET /courses/_search
    {
      "query": {
        "bool": {
          "must": [
            {"match": {"name": "computer"}},
            {"match": {"room": "c8"}}
          ]
        }
      }
    }
    ```
    ```json
    GET /courses/_search
    {
      "query": {
        "bool": {
          "must": [
            {"match": {"name": "accounting"}},
            {"match": {"room": "e3"}}
          ],
          "must_not": [
            {"match": {"professor.name": "bill"}}
          ],
          "should": [
            {"match": {"name": "computer"}}
          ],
          "minimum_should_match": 1
        }
      }
    }
    ```
    ```json
    GET /courses/_search
    {
      "query": {
        "multi_match": {
          "fields": ["name", "professor.department"],
          "query": "accounting"
        }
      }
    }
    ```
    ```json
    GET /courses/_search
    {
      "query": {
        "match_phrase_prefix": {
          "course_description": "build a transaction led"
        }
      }
    }
    ```
    ```json
    GET /courses/_search
    {
      "query": {
        "range": {
          "students_enrolled": {
            "gte": 19,
            "lte": 20
          }
        }
      }
    }
    ```
    ```json
    GET /courses/_search
    {
      "query": {
        "bool": {
          "must": [
            {"match": {"name": "accounting"}}
          ],
          "must_not": [
            {"match": {"room": "e7"}}
          ],
          "should": [
            {"range": {
              "course_publish_date": {
                "gte": "2014-05-15"
              }
            }}
          ]
        }
      }
    }
    ```
- Filter
    ```json
    GET /courses/_search
    {
      "query": {
        "bool": {
          "filter": [
            {"term": {"name": "accounting"}}
          ],
          "must": [
            {"match": {"professor.name": "bill"}},
            {"range": {"students_enrolled": {
                "gte": 17}
            }}
          ],
          "must_not": [
            {"match": {"room": "e7"}}
          ]
        }
      }
    }
    ```
- Aggregations DSL

    ```json
    GET /vehicles/_search
    {
      "size": 5, 
      "query": {
        "match_all": {}
      },
      "sort": [
        {
          "price": {
            "order": "desc"
          }
        }
      ]
    }
    ```
    ```json
    GET /vehicles/_search
    {
      "size": 0,
      "query": {
        "match": {
          "color": "red"
        }
      }, 
      "aggs": {
        "popular_cars": {
          "terms": {
            "field": "make.keyword"
          },
          "aggs": {
            "avg_price": {
              "avg": {
                "field": "price"
              }
            },
            "max_price": {
              "max": {
                "field": "price"
              }
            },
            "min_price": {
              "min": {
                "field": "price"
              }
            }
          }
        }
      }
    }
    ```
    ```json
    GET /vehicles/_search
    {
      "size": 0,
      "aggs": {
        "popular_cars": {
          "terms": {
            "field": "make.keyword"
          },
          "aggs": {
            "stats_on_price": {
              "stats": {
                "field": "price"
              }
            }
          }
        }
      }
    }
    ```
    ```json
    GET /vehicles/_search
    {
      "size": 0,
      "aggs": {
        "car_conditions": {
          "terms": {
            "field": "condition.keyword"
          },
          "aggs": {
            "sold_date_ranges": {
              "range": {
                "field": "sold",
                "ranges": [
                  {"from": "2015-01-01",
                    "to": "2015-01-12"
                  },
                  {"from": "2016-01-01",
                    "to": "2017-01-12"
                  }
                ]
              },
              
              "aggs": {
                "stats_price": {
                  "stats": {
                    "field": "price"
                  }
                },
                "make": {
                  "terms": {
                    "field": "make.keyword",
                    "size": 10
                  }
                }
              }
            }
          }
        }
      }
    }
    ```

## Download and Configure Logstash
- Here the [guide](https://www.elastic.co/downloads/logstash)
- Check Java version
  - `java -version`

**Stashing Your First Event**
- A Logstash pipeline has two required elements, `input` and `output`, and one optional element, `filter`. The input plugins consume data from a source, the filter plugins modify the data as you specify, and the output plugins write the data to a destination.
- To test your Logstash installation
  ```bash
  cd logstash-7.10.2
  bin/logstash -e 'input { stdin {}} output { stdout {}}'
  ```
- Configuring Logstash
  - Use `-f` to specify config file
  ```text
  logstash-simple.conf
  input { stdin { } }
  output {
    elasticsearch { hosts => ["localhost:9200"] }
    stdout { codec => rubydebug }
  }
  ```
  - `bin/logstash -f logstash-simple.conf`
  - Logstash Configuration [Examples](https://www.elastic.co/guide/en/logstash/current/config-examples.html)

## Kibana Visualizations and Dashboards
- Kibana is a data visualization dashboard for Elasticsearch.
- Check count of indicies
  - `http://localhost:9200/logstash-*/_count`
- Elastic stack
  - [ELK](https://www.elastic.co/what-is/elk-stack) stack
- __Beats__ is a single-purpose data shippers. They send data from hundreds or thousands of machines and systems to Logstash or Elasticsearch.
  - Install FileBeat
    ```
    - curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.10.2-darwin-x86_64.tar.gz
    - tar xzvf filebeat-7.10.2-darwin-x86_64.tar.gz
    ```
- Start Logstash
  ```
  cd logstash-7.10.2
  bin/logstash -f /Users/augustine/Documents/Code/data-intensive-distributed/Elasticsearch/ELK/data/apache.conf
  ```
  - `sudo bin/logstash -f /Users/augustine/Documents/Code/data-intensive-distributed/Elasticsearch/ELK/data/logstash-cars.conf`
- Start Filebeat
  ```
  cd filebeat-7.10.2
  ./filebeat
  ```
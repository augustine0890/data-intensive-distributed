# Elastic Stack (ELK)

## Elasticsearch with Logstach and Kibana
**Launch the stack**
- Docker
    - Docker way as [detail](https://elk-docker.readthedocs.io/)
    - Using docker-compose [here](https://github.com/deviantony/docker-elk)
- Use AWS Elasticsearch
    - AWS ES is a fully managed service that has Logstash, Elasticsearch, and Kibana builtin.
    - ELK stack wkth Load balancer.

## Amazon Elasticsearch Service
- Create an Amazon ES domain

- Upload data to an Amazon ES domain for indexing
    - Upload single document
        ```bash
        curl -XPUT -u 'master-user:master-user-password' 'domain-endpoint/movies/_doc/1' -d '{"director": "Burton, Tim", "genre": ["Comedy","Sci-Fi"], "year": 1996, "actor": ["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "title": "Mars Attacks!"}' -H 'Content-Type: application/json'
        ```
    - Upload a JSON file that contains multiple documents
        ```json
        POST _bulk
        {"index":{"_index":"movies","_id":"1"}}
        {"director": "Burton, Tim", "genre": ["Comedy","Sci-Fi"], "year": 1996, "actor": ["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "title": "Mars Attacks!"}
        {"index":{"_index":"movies","_id":"2"}}
        {"director":"Frankenheimer, John","genre":["Drama", "Mystery","Thriller",    "Crime"],"year":1962,"actor":   ["Lansbury, Angela","Sinatra, Frank","Leigh,   Janet", "Harvey, Laurence","Silva, Henry","Frees, Paul", "Gregory, James",  "Bissell, Whit","McGiver, John",  "Parrish, Leslie","Edwards, James","Flowers,  Bess",  "Dhiegh, Khigh","Payne, Julie","Kleeb, Helen","Gray,  Joe","Nalder,     Reggie","Stevens, Bert","Masters,  Michael","Lowell, Tom"],"title":"The  Manchurian     Candidate"}
        {"index":{"_index":"movies","_id":"3"}}
        {"director":"Baird, Stuart","genre":["Action","Crime",  "Thriller"],"year":1998,  "actor":["Downey Jr., Robert",  "Jones, Tommy Lee","Snipes, Wesley",    "Pantoliano,  Joe","Jacob, Irène","Nelligan, Kate","Roebuck,   Daniel",    "Malahide, Patrick","Richardson, LaTanya",    "Wood, Tom","Kosik, Thomas",  "Stellate, Nick", "Minkoff, Robert","Brown, Spitfire","Foster, Reese",     "Spielbauer, Bruce","Mukherji, Kevin","Cray, Ed",   "Fordham, David","Jett,     Charlie"],"title":"U.S.    Marshals"}
        {"index":{"_index":"movies","_id":"4"}}
        {"director":"Ray, Nicholas","genre":["Drama","Romance"],    "year":1955,"actor":    ["Hopper, Dennis","Wood,    Natalie","Dean, James","Mineo, Sal","Backus, Jim",     "Platt, Edward","Ray, Nicholas","Hopper, William",  "Allen, Corey","Birch,     Paul","Hudson, Rochelle",  "Doran, Ann","Hicks, Chuck","Leigh, Nelson",      "Williams, Robert","Wessel, Dick","Bryar, Paul",   "Sessions, Almira","McMahon,   David","Peters Jr.,     House"],"title":"Rebel Without a Cause"}
        ```
- Search documents in an Amazon ES domain
    ```json
    GET /movies/_search?q=mars
    ```
- Delete an Amazon ES domain
    - Because the _movies_ domain for test purpose, you should delete it when you are finished experimenting to avoid incurring charges.
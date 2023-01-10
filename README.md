# komusimilaritysentenceapi
Api for check similarity of sentences on komu dashboard project:


--- Solution:
Using conponentL: BERD model of Sentence Transformer library
Then transformer a sentence to vector type
Embedding this vector by model BERD 
Using Calculate Cosine Similarity to get ouput
=> Ouput is list % similiraty of 1 sentences today daily with sentences corresponding want to compare with today daily.   


--- Run code project in Local:
Python 3.10.7 <The latest version is preferred>
IDE: Pycharm or VS code

--- Library:
pip install Flask
pip install numpy
pip install -U sentence-transformers


--- IP local address
IP default flask: Running on http://127.0.0.1:7777
(or my IP local Running on http://10.10.41.10:7777 )


--- Url to call api on Postman:
POST: http://127.0.0.1:7777/api/services/app/ApiPython/PostSimilarityRatioSentences
or POST: http://10.10.41.10:7777/api/services/app/ApiPython/PostSimilarityRatioSentences (my IP Local)


--- Example Test code on postman:
    *note:  input: List<string> , output: list double % of similarity
            default list[0] is daily today sentence is compared
            range(1, len(list)) is list sentences to compare with list[0] - daily today

    Input List<string> with list[0] is daily today is string to compare with other in lists:  
    [
    "He is very handsome",
    "you are very beautifull",
    "she swore she just saw her sushi move",
    "This building is in disrepair",
    "This building is in disrepair",
    "they are building this building",
    "I saw the weather forecast that it’s going to be fine today",
    "He is very handsome",
    "Good weather"
    ]

    Output: 
    [
    0.8558,
    0.1772,
    0.3042,
    0.3042,
    0.2485,
    0.4171,
    1.0,
    0.7602
    ]
---


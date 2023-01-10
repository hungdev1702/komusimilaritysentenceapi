from flask import *
import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

def GetModel():
    # Use conponent model with Bert model
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    return model

def DisplayInput(listDailySentences):
    print("Daily today:", listDailySentences[0])
    print("-- List of sentences need to compare:")
    for i in range(1, len(listDailySentences)):
        print(i, listDailySentences[i])

def AnalysisDataByEmbedding(listDailySentences, model):
    sim = np.zeros(len(listDailySentences) - 1)
    sentences = listDailySentences
    embeddingsDailyList = model.encode(sentences)

    dailyTodayEmbedding = embeddingsDailyList[0]
    for i in range(1, len(sentences)):
        sim[i - 1] = cos_sim(dailyTodayEmbedding, embeddingsDailyList[i])
    sim = sim.round(4)
    return sim


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    message = 'Successfully loaded for Home Page'
    return message

@app.route('/api/services/app/ApiPython/PostSimilarityRatioSentences', methods=['POST'])
def PostSimilarityRatioSentences():
    print("starting")
    input_data = request.get_json()
    dailies_list = input_data
    # dailies_list[0] is default daily today
    # Range(1, len) is sentences daily to compare

    # Display all daily:
    # DisplayInput(dailies_list)

    # Analysis data:
    data_analysed = AnalysisDataByEmbedding(dailies_list, model)
    result = data_analysed.tolist()
    print("successed")
    return result


if __name__ == "__main__":
    print("get model")
    model = GetModel()
    print(model)
    app.run(host='0.0.0.0', port=7777)

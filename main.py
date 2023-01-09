from flask import *
import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import json

def GetModel():
    # Use conponent model with Bert model
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    return model

def DisplayInput(dailySentence, listDailySentences):
    print("0", dailySentence)
    print("-- List of sentences need to compare:")
    for i in range(len(listDailySentences)):
        print(i + 1, listDailySentences[i])

def AnalysisDataByEmbedding(dailySentence, listDailySentences, model):
    sim = np.zeros((len(listDailySentences)))
    sentences = listDailySentences
    sentences.append(dailySentence)
    embeddingsDailyList = model.encode(sentences)

    dailyTodayEmbedding = embeddingsDailyList[len(sentences) - 1]
    for i in range(len(sentences) - 1):
        sim[i] = cos_sim(dailyTodayEmbedding, embeddingsDailyList[i])

    sim = sim.round(4)
    return sim

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded for Home Page'}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/api/services/app/ApiPython/GetSimilarityRatioSentences', methods=['POST'])
def GetSimilarityRatioSentences():
    # convert data from json to string and list<string>
    input_data = json.loads(request.data)
    daily_dictionary = input_data[0]
    daily_list_dictionary = input_data[1]
    daily_today = daily_dictionary['dailytoday']
    dailies_list = [
        daily_list_dictionary['daily1'],
        daily_list_dictionary['daily2'],
        daily_list_dictionary['daily3'],
        daily_list_dictionary['daily4'],
        daily_list_dictionary['daily5'],
        daily_list_dictionary['daily6'],
        daily_list_dictionary['daily7']]

    # Display all daily:
    # DisplayInput(daily_today, dailies_list)

    # Analysis data:
    data_analysed = AnalysisDataByEmbedding(daily_today, dailies_list, model)
    result = data_analysed.tolist()
    print("success")
    return result

if __name__ == "__main__":
    print("start")
    model = GetModel()
    print(model)
    app.run(host='0.0.0.0', port=7777)

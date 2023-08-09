#2zAP6eQuJZ0YtWdf1G34RY28avtUy0DlJzWN5FlDiJg
import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key('2zAP6eQuJZ0YtWdf1G34RY28avtUy0DlJzWN5FlDiJg')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner_analysis(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion_analyse(self,text):
        response  = paralleldots.emotion(text)
        return response
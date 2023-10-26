from questions import q, default_answer
from fuzzywuzzy import fuzz

class ChatBot():

    def Answer(self, user_text):
        self.user_text = user_text

        while True:


            if self.user_text == "Соедините меня с оператором":
                break

            if fuzz.partial_ratio(user_text, q.get(1)[0]) >= 70:
                answer = q.get(1)[1]
            elif fuzz.partial_ratio(user_text, q.get(2)[0]) >= 70:
                answer = q.get(2)[1]
            else:
                answer = default_answer
            
            print(answer)
            return answer
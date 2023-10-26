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
            elif fuzz.partial_ratio(user_text, q.get(3)[0]) >= 70:
                answer = q.get(3)[1]
            elif fuzz.partial_ratio(user_text, q.get(4)[0]) >= 70:
                answer = q.get(4)[1]
            elif fuzz.partial_ratio(user_text, q.get(5)[0]) >= 70:
                answer = q.get(5)[1]
            elif fuzz.partial_ratio(user_text, q.get(6)[0]) >= 70:
                answer = q.get(6)[1]
            elif fuzz.partial_ratio(user_text, q.get(7)[0]) >= 70:
                answer = q.get(7)[1]
            else:
                answer = default_answer
            
            print(answer)
            return answer
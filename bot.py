from questions import q, default_answer, faq
from fuzzywuzzy import fuzz
from sending import sendtomail

class ChatBot():

    def Answer(self, user_text):
        self.user_text = user_text

        while True:


            if self.user_text == "Соедините меня с оператором":
                break

            if fuzz.partial_ratio(user_text, q.get(1)[0]) >= 70:
                answer = q.get(1)[1]
                faq.append(1)
            elif fuzz.partial_ratio(user_text, q.get(2)[0]) >= 70:
                answer = q.get(2)[1]
                faq.append(2)
            elif fuzz.partial_ratio(user_text, q.get(3)[0]) >= 70:
                answer = q.get(3)[1]
                faq.append(3)
            elif fuzz.partial_ratio(user_text, q.get(4)[0]) >= 70:
                answer = q.get(4)[1]
                faq.append(4)
            elif fuzz.partial_ratio(user_text, q.get(5)[0]) >= 70:
                answer = q.get(5)[1]
                faq.append(5)
            elif fuzz.partial_ratio(user_text, q.get(6)[0]) >= 70:
                answer = q.get(6)[1]
                faq.append(6)
            elif fuzz.partial_ratio(user_text, q.get(7)[0]) >= 70:
                answer = q.get(7)[1]
                faq.append(7)
            else:
                answer = default_answer
                #sendtomail(user_text)
            
            print(answer)
            return answer
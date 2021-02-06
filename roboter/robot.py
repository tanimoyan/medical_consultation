from roboter import to_csv

class MedicalRobot(object):
    def __init__(self):
        self.ranking_model = to_csv.RankingModel()

    # to_csv.pyを呼び出す
    def questions(self):
        new_question = self.ranking_model.get_most_questions()
        if not new_question:
            return None

    # 結果をcsvに出力
    def write_csv(self, name):
        if name:
            self.ranking_model.increment(name)


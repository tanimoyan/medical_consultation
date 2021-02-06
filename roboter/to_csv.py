import collections
import csv
import os
import pathlib


RANKING_COLUMNS_NAME = 'NAME'
RANKING_COLUMNS_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'medical.csv'

# csvファイルがない場合は新たにcsvファイルを作成するクラス
class CsvModel(object):
    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(self.csv_file):
            pathlib.Path(self.csv_file).touch()

# Csvmodelを親クラスに、csvファイルを読み込み書き込むクラス
class RankingModel(CsvModel):
    def __init__(self, csv_file=None, *args, **kwargs):
        if not csv_file:
            csv_file = self.get_csv_file_path()
        super().__init__(csv_file, *args, **kwargs)
        self.columns = [RANKING_COLUMNS_NAME, RANKING_COLUMNS_COUNT]
        self.data = collections.defaultdict(int)
        self.load_data()

    # csvファイルのパスを通す
    def get_csv_file_path(self):
        csv_file_path = None
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass

        if not csv_file_path:
            csv_file_path = RANKING_CSV_FILE_PATH
        return csv_file_path

    # csvファイルを読み込む(読み込まないと更新されない)
    def load_data(self):
        with open(self.csv_file, 'r+') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[row[RANKING_COLUMNS_NAME]] = int(row[RANKING_COLUMNS_COUNT])
        return self.data

    # csvファイルに書き込む
    def save(self):
        if not os.path.exists(self.csv_file):
            pathlib.Path(self.csv_file).touch()
        with open(self.csv_file, 'w+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.columns)
            writer.writeheader()

            for name, count in self.data.items():
                writer.writerow({
                    RANKING_COLUMNS_NAME: name,
                    RANKING_COLUMNS_COUNT: count
                })

    # リストがない場合は空のリストを渡し、リストが存在する場合は降順に並べる
    def get_most_questions(self, not_list=None):
        if not_list is None:
            not_list = []

        if not self.data:
            return None

        # 降順にソート
        sorted_data = sorted(self.data, key=self.data.get, reverse=True)
        for name in sorted_data:
            if name in not_list:
                continue
            return name

    # チェックボックスにチェックを入れた回答をdefaultdict関数を用いてリストに加える
    def increment(self, name):
        self.data[str(name)] += 1
        self.save()
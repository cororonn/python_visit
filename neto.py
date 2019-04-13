import os
from urllib.request import urlretrieve
from urllib.parse import urlparse
from zipfile import ZipFile

def download_file(url, output_dir, overwrite=False):
  # URLからファイル名を取得
  parse_result = urlparse(url)
  file_name = os.path.basename(parse_result.path)
  # 出力先ファイルパス
  destination = os.path.join(output_dir, file_name)

  # 無意味なダウンロードを防ぐため、上書き（overwrite）の指定か未ダウンロードの場合のみダウンロードを実施する
  if overwrite or not os.path.exists(destination):
    # 出力先ディレクトリの作成
    os.makedirs(output_dir)
    # ダウンロード
    urlretrieve(url, destination)

  return destination

zip_file = download_file('https://archive.ics.uci.edu/ml/machine-learning-databases/00360/AirQualityUCI.zip', 'UCI_data/')
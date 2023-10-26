import json
from konlpy.tag import Kkma, Okt, Hannanum, Komoran
import os
from tqdm import tqdm  # tqdm 라이브러리 추가

# 형태소 분석기 초기화
kkma = Kkma()
okt = Okt()
hannanum = Hannanum()
komoran = Komoran()

# 데이터 디렉토리 경로
base_directory = '/content/drive/MyDrive/jeju/'

# 원하는 데이터 폴더 선택 (예: 'Training' 또는 'Validation')
data_directory = os.path.join(base_directory, 'Training')

# 형태소 분석 결과 저장 딕셔너리
results = {}

def analyze_text(text):
    kkma_result = kkma.morphs(text)
    okt_result = okt.morphs(text)
    hannanum_result = hannanum.morphs(text)
    komoran_result = komoran.morphs(text)
    
    return {
        'Kkma': kkma_result,
        'Okt': okt_result,
        'Hannanum': hannanum_result,
        'Komoran': komoran_result
    }

# 선택한 데이터 폴더 내의 JSON 파일 목록 가져오기
data_files = [file for file in os.listdir(data_directory) if file.endswith('.json')]

# 최대 100개의 JSON 파일만 선택
data_files = data_files[:100]

# 형태소 분석 결과 저장
results['Selected'] = {}

for data_file in tqdm(data_files, desc="데이터 처리중"):
    with open(os.path.join(data_directory, data_file), 'r', encoding='utf-8') as file:
        data = json.load(file)
        for idx, utterance in enumerate(data['utterance']):  # 모든 데이터 사용
            text = utterance['dialect_form']
            result = analyze_text(text)
            results['Selected'][f'Utterance_{idx + 1}'] = result

# 결과 출력
for data_dir, data_results in results.items():
    print(f"{data_dir} 데이터 형태소 분석 결과:")
    for utterance, morpheme_data in data_results.items():
        print(f"\n{utterance}:")
        for morpheme, result in morpheme_data.items():
            print(f"{morpheme} 형태소 분석 결과: {result}")
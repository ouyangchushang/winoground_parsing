import os
import stanza
from tqdm import tqdm

# 初始化stanza pipeline
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency',use_gpu=True)

# 指定要处理的文件夹
folder_path = './'

# 遍历文件夹中的所有文件
for filename in tqdm(os.listdir(folder_path)):
    # 只处理txt文件
    if filename.endswith('.txt'):
        # 读取文件中的句子
        with open(os.path.join(folder_path, filename), 'r') as f:
            sentences = f.readlines()
        # 对每个句子进行解析
        parsed_sentences = [(sentence, nlp(sentence).sentences[0].constituency) for sentence in sentences]
        # 将解析结果和原句子写入新的文件
        with open(os.path.join(folder_path, 'parsed_' + filename), 'w') as f:
            for sentence, parsed_sentence in parsed_sentences:
                f.write(sentence.strip() + '\n' + str(parsed_sentence) + '\n\n')

import json

# 创建一个字典来存储每个标签的caption
tag_dict = {}

# 读取newtag.json文件
with open('newtag.json', 'r') as f:
    newtag_data = json.load(f)

# 按行读取example.jsonl文件
with open('examples.jsonl', 'r') as f:
    for line in f:
        # 解析每一行的json数据
        example_data = json.loads(line)
        # 获取id
        id = example_data['id']
        # 如果这个id在newtag.json中没有对应的标签
        if not newtag_data[str(id)]:
            # 将这个id对应的caption添加到"NoTag"的列表中
            if "NoTag" not in tag_dict:
                tag_dict["NoTag"] = []
            tag_dict["NoTag"].append(example_data['caption_0'])
            tag_dict["NoTag"].append(example_data['caption_1'])
        else:
            # 遍历这个id在newtag.json中对应的每个标签
            for tag in newtag_data[str(id)]:
                # 如果这个标签还没有在字典中，就在字典中创建一个新的键
                if tag not in tag_dict:
                    tag_dict[tag] = []
                # 将这个id对应的caption添加到标签的列表中
                tag_dict[tag].append(example_data['caption_0'])
                tag_dict[tag].append(example_data['caption_1'])

# 遍历字典中的每个标签
for tag, captions in tag_dict.items():
    # 创建一个新的txt文件，文件名是标签的名字
    with open(f'{tag}.txt', 'w') as f:
        # 将这个标签对应的所有caption写入文件
        for caption in captions:
            f.write(caption + '\n')

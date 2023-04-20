import os
os.environ['OPENAI_API_KEY'] = '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'
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import (UnstructuredWordDocumentLoader, TextLoader)
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter

folder = 'docs'
loaders = [UnstructuredWordDocumentLoader(os.path.join(folder, fn)) for fn in os.listdir(folder) if fn.endswith('.docx')]
text_loaders = [TextLoader(os.path.join(folder, fn), encoding='utf-8') for fn in os.listdir(folder) if fn.endswith('.txt')]

index = VectorstoreIndexCreator(
    text_splitter=CharacterTextSplitter(chunk_size=400, chunk_overlap=0)
).from_loaders(loaders+text_loaders)

while True:
    # 从屏幕上接收一个字符串输入
    query = input("请输入一句话，或输入'q'结束输入：")
    
    # 如果用户输入 'q'，退出循环
    if query == 'q':
        print('感谢您的使用')
        break

    # 使用查询搜索文本索引
    # results = index.query(query)
    # print(index.query(query))
    if len(query) > 0 :
        try:
            print(index.query_with_sources(query))
        except:
            continue



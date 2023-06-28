import json
import re
import os
import openai
import time
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

#arquivo que contem os dados de testes
filename = 'dataset.jsonl'
expressao_regex = r'"""([^"]*)"""'
 
#transformando cada linha do arquivo em um dicionario  
data = [json.loads(line)
        for line in open(filename, 'r', encoding='utf-8')]

arquivo = open("tradução.txt", "a")

#imprimindo o campo prompt de cada dicionario
for item in data:
    resultado = re.search(expressao_regex, item['prompt'])
    if resultado:
    # Imprimir a string encontrada
        print('Iniciando uma tradução '+ item['task_id'])
        # print(resultado.group(1))
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Traduza para portugues do brasil {} .". format(resultado.group(1))},
        ]
        )
        arquivo.write( item['task_id'] +"   Tradução= " + completion.choices[0].message.content + "\n") 
        print(item['task_id'] + " Traduzido com sucesso!")
        time.sleep(30) # 20 requisições por minuto (RPM) e 40000 tokens por minuto (TPM).
    else:
        print('Nenhuma string delimitada por """ foi encontrada para o problema  '+item['task_id'])
  
arquivo.close()








import json


#arquivo que contem os dados de testes
filename = 'dataset.jsonl'
 
#transformando cada linha do arquivo em um dicionario  
data = [json.loads(line)
        for line in open(filename, 'r', encoding='utf-8')]

arquivo = open("problemas.txt", "a")

#imprimindo o campo prompt de cada dicionario
for item in data:
    arquivo.write( item['task_id'] + "\n" + item['prompt']  + "\n" +  item['test'] + "\n\n")  
   
  
arquivo.close()








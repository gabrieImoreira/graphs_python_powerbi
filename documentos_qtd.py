# O código a seguir para criar um dataframe e remover as linhas duplicadas sempre é executado e age como um preâmbulo para o script: 

#dataset = pandas.DataFrame(Carteira de Identidade)
#dataset = dataset.drop_duplicates()

import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

client = MongoClient()
db = client.documentos_pendentes
historico = db.get_collection('historico')
base = historico.find({})
df = pd.DataFrame(base)
list_len = []
list_len.append(len(df[df['Carteira de Identidade'] == 'False']))
list_len.append(len(df[df['Cédula de identidade do responsável financeiro pelo contrato'] == False]))
list_len.append(len(df[df['Certidão de Nascimento ou Casamento'] == 'False']))
list_len.append(len(df[df['Certidão de Quitação Eleitoral'] == 'False']))
list_len.append(len(df[df['Certificado de dispensa de incorporação'] == 'False']))
list_len.append(len(df[df['Contrato de Prestação de Serviços Educacionais'] == False]))
list_len.append(len(df[df['CPF'] == 'False']))
list_len.append(len(df[df['CPF ou documento que contenha o CPF do responsável financeiro pelo contrato'] == False]))
list_len.append(len(df[df['Histórico Escolar'] == 'False']))
list_len.append(len(df[df['Histórico Escolar de Conclusão do Ensino Médio '] == 'False']))
#list_len.append(len(df[df['Carteirinha de Vacinação - Atualizada.'] == False]))
list_len.append(len(df[df['Passaporte'] == 'False']))
list_len.append(len(df[df['Registro Nacional Migratório - RNM, se estrangeiro'] == 'False']))
list_len.append(len(df[df['Visto de estudante concedido pela autoridade consular brasileira, se estrangeiro'] == 'False']))
list_name = ['Carteira de Identidade','Identidade do responsável',
          'Certid. de Nasc./Casamento','Certidão de Quitação Eleitoral',
          'Certif. de dispensa de incorp.','Contrato de Prestação S.E.',
          'CPF','CPF do responsável',
          'Histórico Escolar','Hist. Escolar de Conclusão E.M',
          'Passaporte','RNM, se estrangeiro',
          'Visto (estrangeiros)'
         ]
consolidado = pd.DataFrame({'Documento': list_name,
                   'Quantidade': list_len})
consolidado = consolidado.sort_values(by='Quantidade',ascending=False)
fig, ax = plt.subplots(figsize =(55,9))
 
# Horizontal Bar Plot
ax.barh(consolidado['Documento'], consolidado['Quantidade'], color='#A38600')
 

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5, labelsize=0)
ax.yaxis.set_tick_params(pad = 5, labelsize=30)
 
# Show top values
ax.invert_yaxis()
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.5, i.get_y()+0.6,
             str(round((i.get_width()), 2)),
             fontsize = 30, fontweight ='bold',
             color ='grey')
 
# Show Plot
#plt.xscale('symlog')
#plt.xlim(min(consolidado['Quantidade']), max(consolidado['Quantidade']))
plt.show()
# Cole ou digite aqui seu código de script:

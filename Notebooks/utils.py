from pyspark.sql import functions as f # importo a biblioteca functions

# crio a função que vai receber os dados para serem avaliados
def calcula_mostra_metricas(modelo_lr, df_transform_modelo, normalize=False, percentage=True):
# os passos para montagem da matriz de confusão são os mesmos da aula
  tp = df_transform_modelo.select('label', 'prediction').where((f.col('label') == 1) & (f.col('prediction') == 1)).count()
  tn = df_transform_modelo.select('label', 'prediction').where((f.col('label') == 0) & (f.col('prediction') == 0)).count()
  fp = df_transform_modelo.select('label', 'prediction').where((f.col('label') == 0) & (f.col('prediction') == 1)).count()
  fn = df_transform_modelo.select('label', 'prediction').where((f.col('label') == 1) & (f.col('prediction') == 0)).count()

  valorP = 1
  valorN = 1

  if normalize:
    valorP = tp + fn
    valorN = fp + tn

  if percentage and normalize:
    valorP = valorP / 100
    valorN = valorN / 100

  # ‘s’ será minha string de retorno
  # ela vai coletar e montar minha matriz de confusão
  # e também os valores de acurácia, precisão, recall e F1-score
  s = ''

  # construção da minha string da matriz de confusão  
  s += ' '*20 + 'Previsto\n'
  s += ' '*15 +  'Churn' + ' '*5 + 'Não-Churn\n'
  s += ' '*4 + 'Churn' + ' '*6 +  str(int(tp/valorP)) + ' '*7 + str(int(fn/valorP)) + '\n'
  s += 'Real\n'
  s += ' '*4 + 'Não-Churn' + ' '*2 + str(int(fp/valorN)) +  ' '*7 + str(int(tn/valorN))  + '\n'
  s += '\n'

  # coleto o resumo das métricas com summary
  resumo_lr_treino = modelo_lr.summary

  # adiciono os valores de cada métrica a minha string de retorno
  s += f'Acurácia: {resumo_lr_treino.accuracy}\n'
  s += f'Precisão: {resumo_lr_treino.precisionByLabel[1]}\n'
  s += f'Recall: {resumo_lr_treino.recallByLabel[1]}\n'
  s += f'F1: {resumo_lr_treino.fMeasureByLabel()[1]}\n'

  return s

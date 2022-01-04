# PLN_Audio

Projeto acadêmico desenvolvido em parceria com o Banco Safra.
O objetivo do projeto foi de realizar análise de sentimento de áudios de whatsapp através de processamento de linguagem natural de forma automatizada, utilizando a linguagem de programação python.
O processo de criação da solução foi divido em três partes:

- Transcrição dos áudios para texto.
- Tratamento dos textos para análises.
- Criação do modelo estatistico utilizando machine learning.

Funcionamento:
O algoritmo de transcrição de texto carrega todos os arquivos de áudios em formato .wav, realiza a transcrição e salva um arquivo de texto para cada arquivo carregado.
O algoritmo de tratamento de texto seleciona todos os arquivos .csv no diretório onde os arquivos foram salvos, realiza o tratamento para que os dados fiquem no formato correto para as análises.
O algoritmo de tratamento das resenhas para treino do modelo, realiza o mesmo procedimento do algoritmo de tratamento de textos, com adptações para o formato dos dados.
O algoritmo de criação do modelo de análise é treinado com uma base de dados de 800 resenhas.

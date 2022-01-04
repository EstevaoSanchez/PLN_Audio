import speech_recognition as sr 
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import wave

# Criando um objeto speech recognition
r=sr.Recognizer()

lista_arquivos=[x for x in os.listdir('/home/estevao/VSC_PROJECTS/PLN_audio/audios') if x.endswith(".wav")]

for arquivo in lista_arquivos:
    path_arq = f"/home/estevao/VSC_PROJECTS/PLN_audio/audios/{arquivo}"   
    whole_text = []


    # Função que divide os áudios em pedaços e usa o speech recognition
    def get_large_audio_transcription(path = 'Untitled.wav',lang = 'pt-Br'):
    # def get_large_audio_transcription(path):
        # Abre o arquivo de áudio usando o pydub
        sound = AudioSegment.from_wav(path) 
        # Divide o arquivo quando há 500 milisegundos ou mais de silêncio
        chunks = split_on_silence(sound,
            min_silence_len = 500,
            # ajustar de acordo com a necessidade
            silence_thresh = sound.dBFS-14,
            # Define o silêncio com tamanho de 500 milisegundos
            keep_silence=500,)
        pasta_audios = "audio-chunks"
        # criar um diretório para armazer as partes do audio
        if not os.path.isdir(pasta_audios):
            os.mkdir(pasta_audios)
        # Processamento de cada parte do áudio 
        for i, audio_chunk in enumerate(chunks, start=1):
            # Exporta as partes do áudio, enumera e salva no diretório pasta_audios
            chunk_filename = os.path.join(pasta_audios, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # Faz a verificação das partes
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                # Tenta converter para texto
                try:
                    text = r.recognize_google(audio_listened, language=lang)
                
                except sr.UnknownValueError as erro:
                    print("Error:", str(erro))
                else:
                    text = f"{text.capitalize()}. "
                    #print(chunk_filename, ":", text)
                    whole_text.append(text)
        return whole_text
        
        
    get_large_audio_transcription(path = path_arq,lang = 'pt-Br')

    pasta_texto = "arquivos_texto"
        # criar um diretório para armazer os textos
    if not os.path.isdir(pasta_texto):
        os.mkdir(pasta_texto)

    print(whole_text)
    # Exporta o texto para a pasta_texto
    caminho_texto='/home/estevao/VSC_PROJECTS/PLN_audio/arquivos_texto/'
    with open(f"{caminho_texto}{arquivo}.csv","a") as inv:
        for linha in whole_text:
            inv.write(linha + "\n")
    

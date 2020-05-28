import argparse
import os
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import sys
from pydub import AudioSegment

parser = argparse.ArgumentParser(description="Converter videos/audios em texto com google-cloud-speech.")
parser.add_argument("--input", required=True, help="Diretório do arquivo de audio")
parser.add_argument("--credentials", required=True, help="Diretório das credenciais do google em .json")
args = parser.parse_args()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = args.credentials
client = speech_v1.SpeechClient()

# Converter arquivo
isFileExist = os.path.isfile(args.input)
if isFileExist:
    result_final = ''
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC

    sample_rate_hertz = 48000
    language_code = 'pt-BR'
    config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}

    # Converting ogg in flac
    name = args.input.split(".")
    path_flac = name[-1] + '.flac'
    AudioSegment.from_ogg(args.input).export(path_flac, format='flac')

    with io.open(path_flac, "rb") as f:
        content = f.read()

    audio = { 'content': content}

    operation = client.long_running_recognize(config, audio)
    results = operation.result()
    for result in results.results:
        result_final += result.alternatives[0].transcript
    print(result_final)    
    sys.exit(0)
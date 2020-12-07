import boto3

polly = boto3.client('polly')

result = polly.synthesize_speech(Text='Hello World!', OutputFormat='mp3', VoiceId='Aditi')

audio = result['AudioStream'].read()
with open("helloworld.mp3","wb") as file:
    file.write(audio)

#if __name__ == '__main__':
#    print('do a thing')
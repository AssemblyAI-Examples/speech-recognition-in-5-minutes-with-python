from utils.utils import *

api_key = "<YOUR-API-KEY>"
audio_file = "audio.mp3"

# Create header with authorization along with AssemblyAI API requests
header = make_header(api_key)

# Upload the audio file to AssemblyAI
upload_url = upload_file(audio_file, header)

# Request a transcription
transcript_response = request_transcript(upload_url, header)

# Create a polling endpoint that will let us check when the transcription is complete
polling_endpoint = make_polling_endpoint(transcript_response)

# Wait until the transcription is complete
wait_for_completion(polling_endpoint, header)

# Request the paragraphs of the transcript
paras = get_paragraphs(polling_endpoint, header)

# Print out the transcript paragraphs
for para in paras:
    print(para['text'], '\n')
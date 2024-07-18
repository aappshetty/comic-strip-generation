"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import time

import google.generativeai as genai
import csv

genai.configure(api_key="AIzaSyDcsEHs9zvFMlC6ihc4p13M3Cvu4xavrcw")

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

def wait_for_files_active(files):
  """Waits for the given files to be active.

  Some files uploaded to the Gemini API need to be processed before they can be
  used as prompt inputs. The status can be seen by querying the file's "state"
  field.

  This implementation uses a simple blocking polling loop. Production code
  should probably employ a more sophisticated approach.
  """
  print("Waiting for file processing...")
  for name in (file.name for file in files):
    file = genai.get_file(name)
    while file.state.name == "PROCESSING":
      print(".", end="", flush=True)
      time.sleep(10)
      file = genai.get_file(name)
    if file.state.name != "ACTIVE":
      raise Exception(f"File {file.name} failed to process")
  print("...all files ready")
  print()

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  upload_to_gemini("METAPHORS REPRESENTATION.csv", mime_type="text/csv"),
]

# Some files have a processing delay. Wait for them to be ready.
wait_for_files_active(files)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        files[0],
      ],
    },
  ]
)



response = chat_session.send_message("Imagine yourself as comic artist creating comics for autistic audience helping them in understanding the scenario and emotional context behind the words through facial expressions and body languages")
#response = chat_session.send_message(" Create a simple creative short comic with comic panels consisting of image description and appropriate simple creative dialogue description catering to autistic kids and use METAPHORS REPRESENTATION.csv for image description of the metaphor used here explaining Elara stared out the dusty train window, the rain blurring the passing fields. She clutched her worn paintbrush, a symbol of her artistic dreams, and a crumpled letter from home, a reminder of her family's expectations. Torn between the vibrant world of colors and the comforting embrace of family, Elara knew this journey held the answer to where she truly belonged.")
response=chat_session.send_message("Create a simple creative short comic with comic panels consisting of appropriate sensible image description and appropriate creative dialogue description catering to autistic individuals and use METAPHORS REPRESENTATION.csv for image description used here explaining how The math problem was a tangled web the student needed to untangle.")
print(response.text)

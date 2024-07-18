"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyDcsEHs9zvFMlC6ihc4p13M3Cvu4xavrcw")

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

chat_session = model.start_chat(
  history=[]
)
response = chat_session.send_message("Imagine yourself as comic artist creating comics for autistic audience helping them in understanding the scenario and emotional context behind the words through facial expressions and body languages")
#response = chat_session.send_message("Create a simple creative short comic with comic panels consisting of image description and apt dialogue description catering to autistic individuals explaining Sarah walked into the coffee shop, feeling a bit apprehensive. She saw her friend Mike sitting at a table by the window. He waved at her and called out, Hey Sarah, over here! Sarah smiled and walked over to him. Hi Mike, she said, taking a seat. They chatted for a while about their day.After a few minutes, Mike asked, Do you want to try the new pumpkin spice latte? Sarah hesitated for a moment but then nodded and said, Sure, why not? Mike got up to order the drinks.While waiting, Sarah glanced around the coffee shop, noticing a young couple in the corner sharing a quiet conversation. Mike returned with the drinks and handed one to Sarah, Here you go, one pumpkin spice latte. Sarah took a sip and her eyes lit up, Wow, this is really good!They continued their conversation, talking about their plans for the weekend. Mike mentioned, I'm thinking of going hiking. Would you like to join? Sarah thought about it and replied, That sounds fun. I'd love to come! As they were leaving the coffee shop, Sarah felt happy and relaxed. She realized how much she enjoyed spending time with Mike.")
#response = chat_session.send_message("Create a simple creative short comic with comic panels consisting of image description and apt dialogue description catering to autistic individuals explaining The city was a living beast during rush hour. Taxis weaved through traffic like hungry sharks, double-decker buses lumbered past like lumbering elephants, and pedestrians scurried across intersections like ants escaping a rainstorm. Amidst the chaos, Alex navigated the sidewalk with the calm focus of a lone wolf, his briefcase a shield against the urban jungle.")
#response = chat_session.send_message("Create a simple creative short comic with comic panels consisting of image description and appropriate creative dialogue description catering to autistic kids explaining The late afternoon sun cast long shadows through the hospital window, painting golden stripes across Arthur's weathered face. In his hand, he held a well-worn picture book, its pages filled with colorful illustrations of playful animals. Across the bed, his daughter, Lily, giggled as he pointed to a fluffy sheep.  Her laughter, like wind chimes in a summer breeze, filled the sterile room with warmth.  Arthur's heart swelled.  Sure, the hospital stay was a worry, but seeing Lily's smile, so full of life and innocence, erased any fear.  In that moment, there was no doubt – his daughter was the light of his life.")
response=chat_session.send_message("Create a simple creative short comic with comic panels consisting of image description and appropriate creative dialogue catering to autistic individuals explaining how The math problem was a tangled web the student needed to untangle.")
print(response.text)
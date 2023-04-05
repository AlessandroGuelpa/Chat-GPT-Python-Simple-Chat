import os
import openai

while True:
  openai.api_key = "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"
  sentence = "Scrivi una descrizione per ";
  t_input = input("Nome prodotto:")
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=sentence + t_input ,
    temperature=0,
    max_tokens=546,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
  )
  message = response.choices[0].text
  print (message.strip())

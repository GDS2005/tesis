from django.shortcuts import render
from decouple import config
import openai

"""
OPEN.AI
"""
# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"

openai.api_key = config('GPT_API_KEY')

def index(request):
    if request.method == 'POST':

        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'system', 'content': 'You answer questions'},
                {'role': 'user', 'content': request.POST.get('user_input')},
            ],
            model=GPT_MODEL,
            temperature=0,
        )

        return render(request, 'index.html', {'generated_text': response['choices'][0]['message']['content']})
    return render(request, 'index.html')
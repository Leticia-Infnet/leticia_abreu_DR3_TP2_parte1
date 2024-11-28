import torch
from fastapi import APIRouter
from transformers import pipeline
from models.chat import TranslationModel, ChatModel, ChatResponseModel

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

router = APIRouter()

generator = pipeline(
    task='translation',
    model='Helsinki-NLP/opus-mt-en-fr',
    device=DEVICE
)


def translation(message: str) -> str:
    return generator(message)


@router.post('/translator')
async def llm_translate(phrase: TranslationModel) -> ChatResponseModel:
    """
Recebe uma frase em inglês e retorna sua tradução para o francês utilizando um modelo
de tradução.
Args:
    phrase (TranslationModel): Objeto contendo a frase a ser traduzida.
        A frase deve ser fornecida em inglês no atributo 'phrase' como JSON em uma requisição POST.
Returns:
    ChatResponseModel: Objeto contendo a tradução.
        A rtradução está no atributo 'assistant' do modelo e é retornada como JSON.
Exemplo:
>>> entrada = 
        {
        "phrase": "Good morning"
        }
>>> resposta = 
        {
        "assistant": "Bonjour"
        }
Note:
        - Se o modelo retornar uma lista, será extraído o texto do primeiro item
    """
    generated_text = translation(phrase.phrase)

    if isinstance(generated_text, list) and 'translation_text' in generated_text[0]:

        response_text = generated_text[0]['translation_text']
    else:
        response_text = str(generated_text)

    response = ChatModel(message=response_text)

    return ChatResponseModel(assistant=response.message)

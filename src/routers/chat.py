import torch
from fastapi import APIRouter
from transformers import pipeline
from models.chat import AutoCompleteModel, ChatModel, ChatResponseModel

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

router = APIRouter()

generator = pipeline(task='text-generation',
                     model='openai-community/gpt2',
                     device=DEVICE
                     )


def autocomplete(message: str) -> dict:
    return generator(message)


@router.post('/autocomplete')
async def llm_autocomplete(phrase: AutoCompleteModel) -> ChatResponseModel:
    """
    Gera uma resposta automática para uma frase de entrada usando um modelo de linguagem.
    Args:
        phrase (AutoCompleteModel): Objeto contendo a frase para autocompletar.
            A frase deve ser fornecida no atributo 'phrase' como JSON em uma requisição POST.
    Returns:
        ChatResponseModel: Objeto contendo a resposta gerada pelo assistente.
            A resposta está no atributo 'assistant' do modelo e é retornada como JSON. 
    Exemplo:
        >>> entrada = 
        {
        "phrase": "I like milk!"
        }
        >>> resposta = 
        {
  "assistant": "I like milk! I like the taste of it. This was my first time buying dairy."
        }
    Note:
        - Se o modelo retornar uma lista, será extraído o texto do primeiro item
    """
    generated_response = autocomplete(phrase.phrase)

    if isinstance(generated_response, list) and 'generated_text' in generated_response[0]:
        response_text = generated_response[0]['generated_text']
    else:
        response_text = str(generated_response)

    response = ChatModel(message=response_text)
    return ChatResponseModel(assistant=response.message)

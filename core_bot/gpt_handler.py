from g4f.client import Client
import g4f.Provider

gpt_client = Client()

provider = g4f.Provider.Pizzagpt


async def get_comment(text):
	print("start gpt")
	response = gpt_client.chat.completions.create(
		model= g4f.models.default,
		provider=provider,
		messages=[{'role': 'user',
		'content': f'Напиши короткий комментарий к этому тексту от '
				f'первого лица, как будто говоришь с другом: {text}'}],
		)
	return response.choices[0].message.content

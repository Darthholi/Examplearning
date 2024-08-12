# https://huggingface.co/spaces/huggingface-projects/gemma-2-2b-it

from gradio_client import Client

client = Client("huggingface-projects/gemma-2-2b-it")
result = client.predict(
		message="Hello!!",
		max_new_tokens=1024,
		temperature=0.6,
		top_p=0.9,
		top_k=50,
		repetition_penalty=1.2,
		api_name="/chat"
)
print(result)
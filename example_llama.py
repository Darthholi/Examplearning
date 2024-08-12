from gradio_client import Client

client = Client("vilarin/Llama-3.1-8B-Instruct")
result = client.predict(
		message="Hello!!",
		system_prompt="You are a helpful assistant",
		temperature=0.8,
		max_new_tokens=1024,
		top_p=1,
		top_k=20,
		penalty=1.2,
		api_name="/chat"
)
print(result)
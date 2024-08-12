# https://huggingface.co/blog/langchain

huggingface_api_key = ''

from huggingface_hub import InferenceClient
import requests

#API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2-large"
API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": f"Bearer {huggingface_api_key}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})
print(output)




"""
model_name = 'gpt2'  # You can choose any model available on Hugging Face

# Initialize the Hugging Face pipeline
hf_pipeline = pipeline('text-generation', model=model_name, use_auth_token=huggingface_api_key)

# Step 4: Create a LangChain Pipeline
class HuggingFaceChain(LLMChain):
    def __init__(self, hf_pipeline):
        self.hf_pipeline = hf_pipeline

    def _call(self, inputs):
        prompt = inputs['prompt']
        response = self.hf_pipeline(prompt, max_length=50)
        return response[0]['generated_text']

# Initialize the LangChain with the Hugging Face pipeline
langchain_pipeline = HuggingFaceChain(hf_pipeline)

# Step 5: Run the Pipeline
input_prompt = "Once upon a time"
result = langchain_pipeline({'prompt': input_prompt})

# Print the result
print(result)
"""
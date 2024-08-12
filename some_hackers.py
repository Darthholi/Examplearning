# https://gist.github.com/win3zz/0a1c70589fcbea64dba4588b93095855

# https://github.com/search?q=%28path%3A*.xml+OR+path%3A*.json+OR+path%3A*.properties+OR+path%3A*.sql+OR+path%3A*.txt+OR+path%3A*.log+OR+path%3A*.tmp+OR+path%3A*.backup+OR+path%3A*.bak+OR+path%3A*.enc+OR+path%3A*.yml+OR+path%3A*.yaml+OR+path%3A*.toml+OR+path%3A*.ini+OR+path%3A*.config+OR+path%3A*.conf+OR+path%3A*.cfg+OR+path%3A*.env+OR+path%3A*.envrc+OR+path%3A*.prod+OR+path%3A*.secret+OR+path%3A*.private+OR+path%3A*.key%29+AND+%28access_key+OR+secret_key+OR+access_token+OR+api_key+OR+apikey+OR+api_secret+OR+apiSecret+OR+app_secret+OR+application_key+OR+app_key+OR+appkey+OR+auth_token+OR+authsecret%29+AND+%28%22sk-%22+AND+%28openai+OR+gpt%29%29&type=code&p=2

from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
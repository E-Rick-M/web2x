
from openai import OpenAI
import requests

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

Model="gemma3:4b"

# using requests to fetch the website content
def get_ai_response(prompt: str, model:str="gemma3:4b",ctx:int=4000) -> str:
    
    # response=requests.post(
    #     "http://localhost:11434/api/generate",
    #     json={
    #         "model": model,
    #         "prompt": prompt,
    #         "stream": False,
    #         "options": {
    #             "num_ctx": ctx,
    #         }
    #     }
    # )
     response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": prompt
            }
            # {
            #     "role": "user",
            #     "content": prompt
            # }
        ],
        stream=False,
    )
     return response.choices[0].message.content.strip()
    
    # try:
    #     response.raise_for_status() 
    # except requests.HTTPError as e:
    #     print(f"Error fetching response from AI: {e}")
    #     return ""
    # except exception as e:
    #     print(f"An unexpected error occurred: {e}")
    #     return ""
    
    # data= response.json()
    
    # return data["response"]

def generate_completion(prompt: str,system:str) -> str:
    response = client.chat.completions.create(
        model=Model,
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=False,
    )
    return response.choices[0].message.content.strip()


def get_website_html(url: str) -> str:
    try:
        response=requests.get(url)
        response.raise_for_status() 
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""


def extract_core_website_content(html: str,history:list) -> str:
    
    # message = f""" You are an expert web content extractor. Your Task is to extract the core content from a given HTML page.
    #         The core content should be the main text, excluding navigation, footers and other non-essential elements like scripts etc.
            
    #         Here is the HTML content:
    #         <html>
    #         {html}
    #         </html>
            
    #         please extract the core content and return it as a plain text."""
    # core_content_extracted=generate_completion(
    #     prompt=html,
    #     system=message
    # )
    # return core_content_extracted
    
    response=get_ai_response(
        model="gemma3:4b",
        prompt=f"""You are an expert web content extractor. Your Task is to extract the core content from a given HTML page.
        The core content should be the main text, excluding navigation, footers and other non-essential elements like scripts etc.
        Here is the HTML content:
        <html>
        {html}
        </html>
        please extract the core content and return it as a plain text.""",
        ctx=20000
    )
    return response

def summarize_content(content: str) -> str:
    
    # summarized_content= generate_completion(
    #     prompt=content,
    #     system="You are an expert summarizer. Your Task is to summarize the provided content into concise and clear summary."
    # )
    # return summarized_content
    response=get_ai_response(
        model="qwen3:4b",
        prompt=f"""You are an expert summarizer. Your Task is to summarize the provided content into concise and clear summary.
        Here is the content:
        <content>
        {content}
        </content>
        Please provide a clear and concise summary of the content. Prefer to use bullet points for clarity and avoid necessary explanations.
        """,
        ctx=20000
    )
    return response

def generate_x_Post(summary: str) -> str:
    # genereted_X_post = generate_completion(
    #     prompt=summary,
    #     system="You are an expert social media post generator. Please generate a concise and engaging post for X (formerly Twitter) based on the following summary. "
    # )
    # return genereted_X_post
    response=get_ai_response(
        model="gemma3:4b-it-qat",
        prompt=f"""You are an expert social media post generator. Please generate a concise and engaging post for X (formerly Twitter) based on the following summary.
        Your task is to generate a post based on a short text summary.
        Your Post must be concise, engaging, and suitable for social media sharing.
        Avoid using hashtags, emojis, or any other special characters.
        
        keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.
        
        Here is the summary:
        <summary>
        {summary}
        </summary>
        Please ensure the post is engaging and suitable for social media sharing."""
    )
    return response

def main():
    history = []
    print("Hello from webcontentextractor!")
    website= input("Enter the website URL: ")
    print(f"Fetching content from {website}...")
    
    try:
        html_content= get_website_html(website)
    except Exception as e:
        print(f"Error fetching website content: {e}")
        return
    
    if not html_content:
        print("No content fetched from the website.")
        return
    
    print("---------------------")
    print("Extracting core content from the Website...")
    print("This may take a few seconds please be patient...")
    history.append({
        "role": "user",
        "content": f"Extract core content from the website: {website}"
    })
    core_content=extract_core_website_content(html_content, history)
    print("Core content extracted successfully!")
    print("---------------------")
    print("Core Content:")
    print(core_content)
    print("---------------------")
    
    print("Summarizing the core content...")
    summary = summarize_content(core_content)
    print("Summary generated successfully!")
    print(summary)
    
    
    print("---------------------")
    print("Generating X post...")
    x_post = generate_x_Post(summary)
    print("X post generated successfully!")
    print("X Post:")
    print(x_post)

if __name__ == "__main__":
    main()

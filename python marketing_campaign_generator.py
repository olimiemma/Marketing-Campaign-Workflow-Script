#Marketing Campaign Workflow Script

import openai
import requests
from fpdf import FPDF
from anthropic import Anthropic
# Import other necessary libraries for Gemma 2 and Llama
# For example: 
# from transformers import AutoTokenizer, AutoModelForCausalLM

# Replace with your actual API keys
openai.api_key = "your_openai_api_key"
anthropic = Anthropic(api_key="your_anthropic_api_key")
dall_e_api_key = "your_dall_e_api_key"

def generate_initial_ideas(product_details):
    response = openai.Completion.create(
        engine="text-davinci-002", #can change model here
        prompt=f"Generate 5 creative marketing campaign ideas for the following product: {product_details}", #can edit prompt here, add or remove dets as you see fit
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7, #PLAY with this to to see different results
    )
    return response.choices[0].text.strip().split("\n")

def refine_ideas(ideas, model="claude"): 
    refined_ideas = []
    for idea in ideas:
        if model == "claude":
            refined_idea = refine_with_claude(idea)
        elif model == "gpt":
            refined_idea = refine_with_gpt(idea)
        elif model == "gemma":
            refined_idea = refine_with_gemma(idea)
        elif model == "llama":
            refined_idea = refine_with_llama(idea)
        else:
            raise ValueError("Unsupported model")
        refined_ideas.append(refined_idea)
    return refined_ideas

def refine_with_claude(idea): #refining
    response = anthropic.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=f"Human: Refine and expand on the following marketing campaign idea: {idea}\n\nAssistant:",
        max_tokens_to_sample=300,
        temperature=0.7
    )
    return response.completion.strip()

def refine_with_gpt(idea): # You dan use different models to refine the ideas, just to give you better checks, 
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Refine and expand on the following marketing campaign idea: {idea}",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def refine_with_gemma(idea): #One of the  smartest model as of this date July 8th, thats why I included it here for further refining
    # Placeholder for Gemma 2 implementation
    # You would need to implement the actual API call or model inference here
    return f"Gemma 2 refined idea: {idea}"

def refine_with_llama(idea): #becauase why not, its llama :)
    # Placeholder for Llama implementation
    # You would need to implement the actual API call or model inference here
    return f"Llama refined idea: {idea}"

def create_visual_representation(idea):
    response = openai.Image.create(
        prompt=f"Create a visual representation for the following marketing campaign idea: {idea}",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def compile_report(refined_ideas, image_url):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Marketing Campaign Ideas", ln=1, align='C')
    
    for i, idea in enumerate(refined_ideas, 1):
        pdf.cell(200, 10, txt=f"Idea {i}:", ln=1)
        pdf.multi_cell(0, 10, txt=idea)
        pdf.ln(10)
    
    pdf.image(image_url, x=10, y=pdf.get_y(), w=190)
    
    pdf.output("marketing_campaign_report.pdf")

def main():
    product_details = input("Enter product details: ")
    model_choice = input("Choose refinement model (claude/gpt/gemma/llama, default is claude): ").lower() or "claude"
    
    initial_ideas = generate_initial_ideas(product_details)
    refined_ideas = refine_ideas(initial_ideas, model=model_choice)
    image_url = create_visual_representation(refined_ideas[0])
    compile_report(refined_ideas, image_url)
    
    print("Marketing campaign report generated successfully!")

if __name__ == "__main__":
    main()

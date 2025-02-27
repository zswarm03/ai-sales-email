import openai

def generate_sales_email(name, product, customer_behavior):
    """Generate a personalized sales email using OpenAI's GPT."""

    prompt = f"""
    You are a sales expert crafting a personalized email.
    The customer's name is {name}.
    The product is {product}.
    Customer behavior: {customer_behavior}.

    Write a warm, engaging, and persuasive sales email.
    """

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Change to "gpt-4" if you have access
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


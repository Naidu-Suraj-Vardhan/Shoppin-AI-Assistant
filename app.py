import gradio as gr
from agent import agent_output

def process_query(message):
    """
    Process the user's message through the agent and return the response.
    """
    try:
        response = agent_output(message)
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Custom CSS for better styling
custom_css = """
#component-0 {
    max-width: 800px;
    margin: auto;
}
.gradio-container {
    font-family: 'Arial', sans-serif;
}
.gr-button {
    background-color: #2e7d32 !important;
    border: none !important;
}
.gr-button:hover {
    background-color: #1b5e20 !important;
}
"""

# Create the Gradio interface with enhanced styling
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown(
        """
        # 🛍️ Shoppin` AI Assistant
        ### Your personal shopping companion powered by AI
        
        I can help you with:
        - Finding products with specific criteria
        - Checking prices and availability
        - Comparing deals across different sites
        - Checking shipping estimates and return policies
        """
    )
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="What would you like to know?",
                placeholder="Ask about products, shipping, prices, or any other e-commerce related questions...",
                lines=3
            )
            submit_btn = gr.Button("Ask Assistant", variant="primary")
            
    with gr.Row():
        output_text = gr.Textbox(
            label="Assistant Response",
            lines=5,
            show_copy_button=True
        )
        
    gr.Examples(
        examples=[
            ["Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code 'SAVE10'?"],
            ["I need white sneakers (size 8) for under $70 that can arrive by next Sunday"],
            ["I found a 'casual denim jacket' at $80 on SiteA. Any better deals?"],
            ["I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?"]
        ],
        inputs=input_text,
        label="Try these examples"
    )

    submit_btn.click(
        fn=process_query,
        inputs=input_text,
        outputs=output_text
    )

if __name__ == "__main__":
    demo.launch(
        share=True,
        server_name="0.0.0.0",
        server_port=7860,
    )
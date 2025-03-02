# Shoppin-AI-Assistant


## Overview

Shoppin' AI Assistant is a personal shopping companion powered by AI that helps users find products, check prices, compare deals, and understand shipping and return policies. Built with a conversational interface, it leverages LangChain and OpenAI's LLM capabilities to provide intelligent e-commerce assistance.

## Features

- **Product Search**: Find products matching specific criteria including price range and size
- **Price Comparison**: Compare prices across different e-commerce sites
- **Discount Checker**: Verify promo codes and calculate final prices
- **Shipping Estimation**: Check shipping feasibility, cost, and delivery times
- **Return Policy Information**: Get return policy details for different sites

## Tech Stack

- **Frontend**: Gradio web interface
- **Backend**: Python with LangChain and LangGraph
- **AI Model**: OpenAI GPT-4o-mini
- **Deployment**: Docker containerization

## Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Option 1: Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Naidu-Suraj-Vardhan/Shoppin-AI-Assistant.git
   cd shoppin-ai-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:7860`

### Option 2: Docker Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Naidu-Suraj-Vardhan/Shoppin-AI-Assistant.git
   cd shoppin-ai-assistant
   ```

2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Build and run with Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. Open your browser and navigate to `http://localhost:7860`

## Usage

The assistant can help with a variety of shopping-related queries. Here are some examples:

- "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code 'SAVE10'?"
- "I need white sneakers (size 8) for under $70 that can arrive by next Sunday"
- "I found a 'casual denim jacket' at $80 on SiteA. Any better deals?"
- "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?"

## Project Structure

- `app.py`: Main Gradio web interface
- `agent.py`: ReAct agent configuration using LangChain and OpenAI
- `tools.py`: Implementation of e-commerce tools (search, shipping, discounts, etc.)
- `Dockerfile` & `docker-compose.yml`: Docker configuration files
- `requirements.txt`: Python dependencies

## Note

This is a demonstration application using simulated e-commerce data. The tools implemented in `tools.py` provide mock responses rather than connecting to actual e-commerce services.



Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

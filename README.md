![Screenshot from 2024-07-08 20-19-54](https://github.com/olimiemma/Marketing-Campaign-Workflow-Script/assets/98601170/e6dd1dab-bbcc-425c-8285-b112ef2b6bc6)
# Marketing Campaign Idea Generator

## Overview

TThis project automates the process of generating and refining creative ideas for marketing campaigns. It leverages various AI models to create, refine, and visualize campaign concepts, demonstrating the integration of multiple AI tools and APIs.

## Features

- Generate initial marketing campaign ideas based on product input
- Refine ideas using a choice of AI models (Claude 3.5 Sonnet, GPT-3.5/4, Gemma 2, or Llama)
- Create visual representations of refined ideas using DALL-E
- Compile results into a formatted PDF report

## Requirements

- Python 3.7+
- OpenAI API key
- Anthropic API key (for Claude)
- DALL-E API key
- Additional API keys or model weights for Gemma 2 and Llama (if using)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/marketing-campaign-generator.git
   cd marketing-campaign-generator
   ```

2. Install required packages:
   ```
   pip install openai anthropic requests fpdf
   ```

3. Set up your API keys:
   - Create a `.env` file in the project root
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     DALL_E_API_KEY=your_dall_e_api_key
     ```

## Usage

1. Run the script:
   ```
   python marketing_campaign_generator.py
   ```

2. Enter the product details when prompted.

3. Choose the AI model for idea refinement (default is Claude 3.5 Sonnet).

4. The script will generate ideas, refine them, create a visual representation, and compile a PDF report.

## Workflow

1. Input product details
2. Generate initial ideas (GPT-3.5)
3. Refine ideas (Choice of Claude 3.5 Sonnet, GPT-3.5/4, Gemma 2, or Llama)
4. Create visual representation (DALL-E)
5. Compile results into a PDF report

## Customization

- To use Gemma 2 or Llama, implement the respective functions in the script and add necessary API calls or model inference code.
- Adjust prompts in the `generate_initial_ideas` and refinement functions to tailor the output to your needs.
- Modify the `compile_report` function to change the format or content of the final report.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

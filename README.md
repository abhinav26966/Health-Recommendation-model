# Blood Test Report Health Recommendation System

This project is a Streamlit-based application that analyzes blood test reports and provides health recommendations using AI-powered agents.

## Prerequisites

- Python 3.12 or higher
- Ollama installed and running locally (for the LLM)

## Setup

1. Clone the repository:

        git clone https://github.com/yourusername/blood-test-analyzer.git


        cd blood-test-analyzer


2. Create a virtual environment:

        python -m venv venv

3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:

        pip install -r requirements.txt

5. Set up environment variables:


    Create a `.env` file in the project root and add any necessary environment variables.

## Running the Application

1. Ensure Ollama is running with the Mistral model:

        ollama run mistral

2. Start the Streamlit application:

        streamlit run main.py

3. Open your web browser and go to `http://localhost:8501` (or the URL provided in the terminal).

## Using the Application

1. Upload a PDF file containing the blood test report.
2. Click the "GET RECOMMENDATIONS" button.
3. Wait for the analysis to complete (this may take a few minutes).
4. View the summary and recommendations provided by the AI agents.

## Project Structure

- `main.py`: The main Streamlit application
- `agents.py`: Defines the AI agents used in the analysis
- `tasks.py`: Defines the tasks performed by the agents
- `requirements.txt`: Lists all the required Python packages

## Troubleshooting

- If you encounter any issues with Ollama or the LLM, ensure that Ollama is properly installed and the Mistral model is available.
- For any other issues, please check the console output for error messages and ensure all dependencies are correctly installed.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

MIT License
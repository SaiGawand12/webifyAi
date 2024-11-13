# WebifyAI - AI Website Generator

WebifyAI is an AI-powered tool that helps users generate dynamic websites based on their specific requirements. Users can specify the type of website they need (e.g., Blog, Portfolio, E-Commerce) and select a framework (e.g., Flask, Django, React, etc.). The tool uses Gemini AI to generate the content for both frontend and backend, including HTML, CSS, JavaScript, and backend code for frameworks like Flask and Django.

## Project Overview

This project aims to make website development easier and faster by using AI to generate the content for different types of websites. Whether you're looking for a simple personal blog, a professional portfolio, or a robust e-commerce platform, WebifyAI can generate the necessary code based on your input.

## Features

- **AI-powered Website Generation**: Automatically generates content for the website based on user input.
- **Multiple Framework Support**: Choose from a variety of frameworks including Flask, Django, React, and others.
- **Customizable Templates**: Generate fully functional websites with frontend and backend code.
- **Downloadable Code**: Once the website is generated, download the entire codebase as a zip file.

## Technologies Used

- **Google Gemini AI**: Used for generating the website content based on the user’s input.
- **Streamlit**: Used for building the user interface to interact with the AI model.
- **Flask/Django**: Backend frameworks supported for generating dynamic web applications.
- **HTML/CSS/JS**: Standard web technologies used for frontend development.
- **JavaScript**: For adding interactivity in the generated websites.

## Setup Instructions

To run the WebifyAI project locally, follow the steps below:

### Prerequisites

Make sure you have the following installed:
- Python 3.7+
- Google Gemini API key (replace `GEMINI_AI_API_KEY` in the script with your actual API key)
- Virtual environment (recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/SaiGawand12/WebifyAI.git
   cd WebifyAI
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google Gemini API Key by replacing `your_actual_gemini_api_key_here` in the script.

5. Run the Streamlit app:
   ```bash
   streamlit run streamlit.py
   ```

6. Open the app in your browser at `http://localhost:8501`.

## Usage Instructions

- After launching the app, you will be prompted to enter the type of website you want (e.g., Blog, Portfolio).
- Select a framework (e.g., Flask, Django, React).
- Click "Generate Website" to generate the content.
- Once the content is generated, you can download the code as a zip file.

## Customization

- You can edit the templates and modify the generated HTML, CSS, and JavaScript to match your brand or personal preferences.
- The backend code for Flask or Django can be extended with additional routes, templates, and models to suit your project’s needs.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request. Make sure to follow the guidelines below:

1. Fork the repository.
2. Create a new branch for your changes (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Streamlit for providing an easy way to create interactive web apps.
- Thanks to Google Gemini AI for powering the content generation.

```

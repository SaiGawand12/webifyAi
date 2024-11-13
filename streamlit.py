import streamlit as st
import zipfile
import os
from io import BytesIO
import google.generativeai as genai

# Replace 'your_actual_gemini_api_key_here' with your actual Gemini AI API key
GEMINI_AI_API_KEY = "AIzaSyB_B2kmeMt1Nukt1xn47zQVavLPiK7Jfo4"

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            color: #4CAF50;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        .description {
            color: #555;
            font-size: 18px;
            text-align: center;
        }
        .input-field {
            margin-bottom: 20px;
        }
        .generate-btn {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
        }
        .generate-btn:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
        }
    </style>
""", unsafe_allow_html=True)

def load_prompt(file_path='prompts.txt'):
    try:
        with open(file_path, 'r') as f:
            prompt = f.read()
        return prompt
    except FileNotFoundError:
        st.error(f"File {file_path} not found.")
        return ""

def generate_website_content(prompt):
    try:
        # Configure Google Gemini AI API
        genai.configure(api_key=GEMINI_AI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        generated_website_content = ""
        for part in response.parts:
            generated_website_content += part.text
        return generated_website_content
    except Exception as e:
        st.error(f"Failed to generate content: {str(e)}")
        return ""

def save_content_as_files(content, output_dir='generated_site', framework='Flask', website_type="Website"):
    try:
        # Create directories for frontend, backend, and assets
        os.makedirs(os.path.join(output_dir, 'frontend'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'backend'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'assets', 'css'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'assets', 'js'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'assets', 'images'), exist_ok=True)

        # Save the generated content to 'frontend' folder
        with open(os.path.join(output_dir, 'frontend', "index.html"), "w", encoding="utf-8") as f:
            f.write(content)

        # If the framework is Flask or Django, add backend code accordingly
        if framework.lower() == 'flask':
            with open(os.path.join(output_dir, 'backend', 'app.py'), "w", encoding="utf-8") as f:
                f.write("""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
                """)
        elif framework.lower() == 'django':
            os.makedirs(os.path.join(output_dir, 'backend', 'myapp'), exist_ok=True)
            with open(os.path.join(output_dir, 'backend', 'myapp', 'views.py'), "w", encoding="utf-8") as f:
                f.write("""
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
                """)
            # You can add more Django-specific code (urls, settings, etc.) if necessary

        # Add some sample assets like CSS and JS files in the assets folder
        with open(os.path.join(output_dir, 'assets', 'css', 'style.css'), "w", encoding="utf-8") as f:
            f.write("""
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}
            """)

        with open(os.path.join(output_dir, 'assets', 'js', 'script.js'), "w", encoding="utf-8") as f:
            f.write("""
document.addEventListener('DOMContentLoaded', function() {
    console.log("Website Loaded!");
});
            """)

        # Add README.md and requirements.txt files
        with open(os.path.join(output_dir, 'README.md'), "w", encoding="utf-8") as f:
            f.write(f"# {website_type} - AI Website Generator\nThis project generates a full website based on user input.\n")

        with open(os.path.join(output_dir, 'requirements.txt'), "w", encoding="utf-8") as f:
            f.write("google-generativeai\nstreamlit\nflask\n")

    except Exception as e:
        st.error(f"Failed to save content: {str(e)}")

def create_zip_file(output_dir='generated_site', website_name="Website"):
    try:
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, _, files in os.walk(output_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, output_dir))
        zip_buffer.seek(0)
        return zip_buffer
    except Exception as e:
        st.error(f"Failed to create zip file: {str(e)}")
        return None

def framework_description(framework):
    """Display HTML description for the selected framework"""
    descriptions = {
        "Django": """
            <h3>Django</h3>
            <p>Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
            It provides built-in features for authentication, ORM, admin panel, and more.</p>
            <p><a href="https://www.djangoproject.com/" target="_blank">Learn more about Django</a></p>
        """,
        "Flask": """
            <h3>Flask</h3>
            <p>Flask is a micro web framework written in Python. It's easy to use and lightweight, making it perfect for building 
            small applications quickly.</p>
            <p><a href="https://flask.palletsprojects.com/" target="_blank">Learn more about Flask</a></p>
        """,
        "React": """
            <h3>React</h3>
            <p>React is a JavaScript library for building user interfaces. It is used to build dynamic and complex web applications.</p>
            <p><a href="https://reactjs.org/" target="_blank">Learn more about React</a></p>
        """,
        "Vue": """
            <h3>Vue.js</h3>
            <p>Vue.js is a progressive JavaScript framework for building modern web applications.</p>
            <p><a href="https://vuejs.org/" target="_blank">Learn more about Vue.js</a></p>
        """,
        "Angular": """
            <h3>Angular</h3>
            <p>Angular is a platform and framework for building single-page client applications using HTML and TypeScript.</p>
            <p><a href="https://angular.io/" target="_blank">Learn more about Angular</a></p>
        """,
        "Spring Boot": """
            <h3>Spring Boot</h3>
            <p>Spring Boot is an open-source Java-based framework used to create stand-alone, production-grade Spring-based applications.</p>
            <p><a href="https://spring.io/projects/spring-boot" target="_blank">Learn more about Spring Boot</a></p>
        """,
        "FastAPI": """
            <h3>FastAPI</h3>
            <p>FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.</p>
            <p><a href="https://fastapi.tiangolo.com/" target="_blank">Learn more about FastAPI</a></p>
        """,
        "Express.js": """
            <h3>Express.js</h3>
            <p>Express is a minimal and flexible Node.js web application framework that provides a robust set of features for building web and mobile applications.</p>
            <p><a href="https://expressjs.com/" target="_blank">Learn more about Express.js</a></p>
        """,
        "Laravel": """
            <h3>Laravel</h3>
            <p>Laravel is a PHP web framework used for building modern, scalable web applications. It includes an ORM, routing, authentication, and more.</p>
            <p><a href="https://laravel.com/" target="_blank">Learn more about Laravel</a></p>
        """,
        "Ruby on Rails": """
            <h3>Ruby on Rails</h3>
            <p>Ruby on Rails is a web application framework written in Ruby. It emphasizes convention over configuration and the use of MVC architecture.</p>
            <p><a href="https://rubyonrails.org/" target="_blank">Learn more about Ruby on Rails</a></p>
        """,
        "ASP.NET": """
            <h3>ASP.NET</h3>
            <p>ASP.NET is a framework for building web applications developed by Microsoft. It's built on the .NET platform and supports C#, F#, and other languages.</p>
            <p><a href="https://dotnet.microsoft.com/en-us/apps/aspnet" target="_blank">Learn more about ASP.NET</a></p>
        """,
        "HTML/CSS/JS": """
            <h3>HTML/CSS/JS</h3>
            <p>HTML, CSS, and JavaScript are the fundamental technologies used to create static websites. HTML defines the structure, CSS styles it, and JavaScript adds interactivity.</p>
        """
    }
    return descriptions.get(framework, "Description not available.")

def main():
    st.markdown('<p class="title">WebifyAI - AI Website Generator</p>', unsafe_allow_html=True)
    st.write("Welcome to WebifyAI. Please fill in the below fields")

    website_type = st.text_input("Enter the type of website", key="website_type", placeholder="e.g. Blog, Portfolio")

    # Dropdown for framework selection
    # website_type = st.selectbox("Select website type", ["Personal Blog", "Portfolio", "E-Commerce", "Business", "Landing Page", "Static Website"], key="website_type")

    frameworks = [
        "Django", "Flask", "React", "Vue", "Angular", "Spring Boot", 
        "FastAPI", "Express.js", "Laravel", "Ruby on Rails", "ASP.NET", "HTML/CSS/JS"
    ]
    framework = st.selectbox("Select a framework", frameworks, key="framework")

    # Display framework description below the dropdown
    description = framework_description(framework)
    st.markdown(f'<div class="framework-description">{description}</div>', unsafe_allow_html=True)

    # Check if the fields are filled before proceeding
    if st.button("Generate Website", key="generate_btn", help="Click to generate the website content"):
        if not website_type or not framework:  # Check if any field is empty
            st.error("Fields can't be empty. Please fill in both fields.")
        else:
            prefix = f"Generate a website using {website_type} type with {framework} framework, "
            prompt = load_prompt()
            final_prompt = f"{prefix}{prompt}"
            content = generate_website_content(final_prompt)
            
            st.write(content)
            
            # Save content to files and create a zip file
            save_content_as_files(content, framework=framework, website_type=website_type)
            zip_buffer = create_zip_file(website_name=website_type)

            if zip_buffer:
                # Provide download button for the zip file with dynamic name
                st.download_button(
                    label=f"Download {website_type} Website Code",
                    data=zip_buffer,
                    file_name=f"{website_type}_website.zip",
                    mime="application/zip"
                )

if __name__ == "__main__":
    main()
<h1>Tesis</h1>

<p>This is a Django project template that demonstrates how to set up a project with Virtualenv, Docker, decouple for managing environment variables, and integration with OpenAI.</p>

<h2>Getting Started</h2>

<p>These instructions will help you get the project up and running on your local machine for development and testing purposes.</p>

<h3>Prerequisites</h3>

<ul>
    <li><a href="https://www.python.org/downloads/">Python</a> (>=3.6)</li>
    <li><a href="https://www.docker.com/get-started">Docker</a></li>
    <li><a href="https://virtualenv.pypa.io/en/latest/">virtualenv</a></li>
    <li><a href="https://pip.pypa.io/en/stable/installing/">pip</a></li>
</ul>

<h3>Installing</h3>

<ol>
    <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/GDS2005/tesis.git
</code></pre>

<ol start="2">
    <li>Create and activate a virtual environment:</li>
</ol>

<pre><code>cd your_project
virtualenv venv
source venv/bin/activate
</code></pre>

<ol start="3">
    <li>Install project dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<h3>Environment Variables</h3>

<p>This project uses the <code>python-decouple</code> library to manage environment variables.</p>

<ol>
    <li>Create a <code>.env</code> file in the root directory:</li>
</ol>

<pre><code>DEBUG=True
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_api_key
</code></pre>

<p>Make sure to replace <code>your_secret_key</code> and <code>your_openai_api_key</code> with your actual values.</p>

<h3>Running with Docker</h3>

<ol>
    <li>Build the Docker image:</li>
</ol>

<pre><code>docker build -t your_image_name .
</code></pre>

<ol start="2">
    <li>Run the Docker container:</li>
</ol>

<pre><code>docker run -p 8000:8000 --env-file .env your_image_name
</code></pre>

<p>The application should now be accessible at <a href="http://localhost:8000">http://localhost:8000</a>.</p>

<h2>Contributing</h2>

<p>Please read <a href="CONTRIBUTING.md">CONTRIBUTING.md</a> for details on our code of conduct, and the process for submitting pull requests to us.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
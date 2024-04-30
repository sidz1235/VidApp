from flask import Flask, render_template, request, jsonify
from analysis import compute

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    # Save the uploaded file to a temporary location
    file_path = 'temp_video.mp4'
    uploaded_file.save(file_path)

    # Call the compute function from analysis.py
    results, duration = compute(file_path)

    # Pass the results to the template
    return render_template('index.html', results=str(results), duration=duration)

if __name__ == '__main__':
    app.run(debug=False)


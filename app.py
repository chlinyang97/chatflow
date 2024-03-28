from flask import Flask, request, send_file, abort
import openai
import subprocess
import tempfile
import os

app = Flask(__name__)

openai.api_key = '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'

def generate_mermaid_code(input_text):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Convert the following text to mermaid code:\n\n{input_text}",
      temperature=0.7,
      max_tokens=150
    )
    mermaid_code = response.choices[0].text.strip()
    return mermaid_code

def generate_mermaid_diagram(mermaid_code, output_file='diagram.png'):
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.mmd') as tmp:
        tmp.write(mermaid_code)
        tmp.flush()

        mmdc_path = '/app/node_modules/.bin/mmdc'
        try:
            subprocess.run([mmdc_path, '-i', tmp.name, '-o', output_file], check=True)
            print(f"Diagram saved as {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error generating diagram: {e}")
            return False
        finally:
            os.unlink(tmp.name)

    return True

@app.route('/generate', methods=['POST'])
def generate():
    if 'file' in request.files:
        file = request.files['file']
        input_text = file.read().decode('utf-8')
    else:
        input_text = request.form.get('text')
    
    if not input_text:
        abort(400, description="No input provided.")
    
    mermaid_code = generate_mermaid_code(input_text)
    output_file = 'mermaid_diagram.png'
    success = generate_mermaid_diagram(mermaid_code, output_file)

    if success:
        return send_file(output_file, mimetype='image/png')
    else:
        abort(500, description="Failed to generate diagram.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

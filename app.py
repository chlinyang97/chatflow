from flask import Flask, send_file, request, abort
import subprocess
import tempfile
import os

app = Flask(__name__)

def generate_mermaid_diagram(mermaid_code, output_file='diagram.png'):
    # Write the Mermaid code to a temporary file
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.mmd') as tmp:
        tmp.write(mermaid_code)
        tmp.flush()  # Flush to ensure all data is written to the file

        # Specify the full path to the Mermaid CLI executable
        mmdc_path = '/app/node_modules/.bin/mmdc'

        # Use the Mermaid CLI to generate the diagram
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
    mermaid_code = request.form.get('code')
    if not mermaid_code:
        abort(400, description="No Mermaid code provided.")

    output_file = 'mermaid_diagram.png'
    success = generate_mermaid_diagram(mermaid_code, output_file)

    if success:
        return send_file(output_file, mimetype='image/png')
    else:
        abort(500, description="Failed to generate diagram.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

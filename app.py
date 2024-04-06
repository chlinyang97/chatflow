from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/render')
def render_mermaid_diagram():
    # Fixed Mermaid code for testing
    mermaid_code = 'graph TD; A-->B; B-->C; C-->D; D-->A;'
    
    # URL of the Mermaid Live Editor render endpoint
    render_url = f'https://mermaid.ink/img/{mermaid_code}'
    
    # Get the diagram image from the Mermaid Live Editor
    response = requests.get(render_url)
    
    if response.status_code == 200:
        # Display the diagram image
        img_url = response.url
        return render_template_string('<img src="{{url}}" alt="Mermaid Diagram"/>', url=img_url)
    else:
        return 'Failed to render diagram', 500
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

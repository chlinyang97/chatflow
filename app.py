

from flask import Flask, render_template_string

app = Flask(__name__)

# Fixed Mermaid code
mermaid_code = '''
graph TB
    sq[Square shape] --> ci((Circle shape))
    subgraph A
        od>Odd shape]-- Two line<br/>edge comment --> ro
        di{Diamond with <br/> line break} -.-> ro(Rounded<br>square<br>shape)
        di==>ro2(Rounded square shape)
    end
    e --> od3>Really long text with linebreak<br>in an Odd shape]
    e((Inner / circle<br>and some odd <br>special characters)) --> f(,.?!+-*ز)
    cyr[Cyrillic]-->cyr2((Circle shape Начало));
    classDef green fill:#9f6,stroke:#333,stroke-width:2px;
    classDef orange fill:#f96,stroke:#333,stroke-width:4px;
    class sq,e green
    class di orange
'''

@app.route('/')
def index():
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mermaid Diagram</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>mermaid.initialize({{startOnLoad:true}});</script>
    </head>
    <body>
        <div class="mermaid">
            {mermaid_code}
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.1', port=port)


# from flask import Flask, request, render_template_string

# app = Flask(__name__)

# @app.route('/generate-diagram', methods=['POST'])
# def generate_diagram():
#     # Get Mermaid code from the request body
#     mermaid_code = request.data.decode('utf-8')
    
#     html_content = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Mermaid Diagram</title>
#         <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
#         <script>mermaid.initialize({{startOnLoad:true}});</script>
#     </head>
#     <body>
#         <div class="mermaid">
#             {mermaid_code}
#         </div>
#     </body>
#     </html>
#     """
#     return render_template_string(html_content)

# if __name__ == '__main__':
#     import os
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.1', port=port)


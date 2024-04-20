from flask import Flask, render_template_string
import asyncio
from pyppeteer import launch
import base64

app = Flask(__name__)

# Function to render Mermaid diagram to SVG using headless browser
async def render_mermaid_to_svg(mermaid_code):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.setContent(f"""
    <div class="mermaid">
        {mermaid_code}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{startOnLoad:true}});
    </script>
    """)
    await page.waitForSelector('.mermaid svg', timeout=5000)  # Adjust timeout as necessary
    svg_content = await page.$eval('.mermaid', lambda div: div.innerHTML)
    await browser.close()
    return svg_content

# Route to generate base64 encoded image of the diagram
@app.route('/')
def index():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
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
    svg_content = loop.run_until_complete(render_mermaid_to_svg(mermaid_code))
    # Encoding SVG to base64
    svg_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    return f"<img src='data:image/svg+xml;base64,{svg_base64}' />"

if __name__ == '__main__':
    app.run(host='0.0.0.1', port=5000)


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


from flask import Flask, send_file
import subprocess
import os

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

    %% Notice that no text in shape are added here instead that is appended further down
    e --> od3>Really long text with linebreak<br>in an Odd shape]

    %% Comments after double percent signs
    e((Inner / circle<br>and some odd <br>special characters)) --> f(,.?!+-*ز)

    cyr[Cyrillic]-->cyr2((Circle shape Начало));

     classDef green fill:#9f6,stroke:#333,stroke-width:2px;
     classDef orange fill:#f96,stroke:#333,stroke-width:4px;
     class sq,e green
     class di orange

'''

@app.route('/')
def index():
    # Save the fixed Mermaid code to a file
    with open('diagram.mmd', 'w') as file:
        file.write(mermaid_code)

    # Convert Mermaid code to a PNG image
    subprocess.run(['mmdc', '-i', 'diagram.mmd', '-o', 'diagram.png'])

    # Send the PNG image as a response
    return send_file('diagram.png', mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.1', port=port)



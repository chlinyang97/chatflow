# import mermaid

# # Function to generate a diagram from Mermaid code
# def generate_diagram(mermaid_code, output_file='diagram.png'):
#     # Initialize the Mermaid object with the provided code
#     m = mermaid.Mermaid(mermaid_code)
    
#     # Generate and save the diagram as an image file
#     m.save_image(output_file)
#     print(f"Diagram saved as {output_file}")

# # Example Mermaid code
# mermaid_code = """
# flowchart TD
#     A[User inputs a search query] --> B[Normalization]
#     B --> C[Index Retrieval]
#     C --> D[Ranking]
#     D --> E[User Profile]
#     E --> F[Context Awareness]
#     F --> G[Formatting]
#     G --> H[Display]
#     H --> I[User Interaction]
#     I --> J[Adjustment and Learning]
#     J --> K[Performance Tracking]
#     K --> L[Continuous Improvement]

#     B -->|correcting typos, expanding abbreviations| B
#     C -->|accesses an index to find products| C
#     D -->|ranked by relevance, popularity, preferences| D
#     E -->|tailor results based on user history| E
#     F -->|consider user's location, time, trends| F
#     I -->|monitor interactions with results| I
#     J -->|improve search algorithm using feedback| J
#     K -->|track search result relevance, speed| K
#     L -->|refine algorithms, update index| L
# """

# # Generate and save the diagram
# generate_diagram(mermaid_code)

import subprocess
import tempfile

def generate_mermaid_diagram(mermaid_code, output_file='diagram.png'):
    # Write the Mermaid code to a temporary file
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.mmd') as tmp:
        tmp.write(mermaid_code)
        tmp.flush()  # Flush to ensure all data is written to the file

        # Use the Mermaid CLI to generate the diagram
        subprocess.run(['mmdc', '-i', tmp.name, '-o', output_file], check=True)
        print(f"Diagram saved as {output_file}")

# Example Mermaid code
mermaid_code = """
flowchart TD
    A[User inputs a search query] --> B[Normalization]
    B --> C[Index Retrieval]
    C --> D[Ranking]
    D --> E[User Profile]
    E --> F[Context Awareness]
    F --> G[Formatting]
    G --> H[Display]
    H --> I[User Interaction]
    I --> J[Adjustment and Learning]
    J --> K[Performance Tracking]
    K --> L[Continuous Improvement]

    B -->|correcting typos, expanding abbreviations| B
    C -->|accesses an index to find products| C
    D -->|ranked by relevance, popularity, preferences| D
    E -->|tailor results based on user history| E
    F -->|consider user's location, time, trends| F
    I -->|monitor interactions with results| I
    J -->|improve search algorithm using feedback| J
    K -->|track search result relevance, speed| K
    L -->|refine algorithms, update index| L
"""

# Generate the diagram
generate_mermaid_diagram(mermaid_code)

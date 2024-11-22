import torch
import cgi
import cgitb
from webDetectproject_part1 import model, preprocess_image


cgitb.enable()  # For detailed error messages in web applications

# HTML form to upload an image
def show_html(result=None):
    print("Content-Type: text/html\n")
    print("""
    <html>
    <head>
        <title>Image Classification</title>
    </head>
    <body>
        <h1>Upload an image to classify (Fake or Real)</h1>
        <form enctype="multipart/form-data" method="post" action="webDetectproject_part2.py">
            <input type="file" name="image" accept="image/*"><br><br>
            <input type="submit" value="Classify Image">
        </form>
    """)

    if result:
        print(f"<h2>Result: {result}</h2>")

    print("""
    </body>
    </html>
    """)

# CGI form to handle user input
form = cgi.FieldStorage()
file_item = form["image"]

# If an image was uploaded, process and classify it
if file_item.filename:
    img_tensor = preprocess_image(file_item.file)
    
    # Perform inference
    with torch.no_grad():
        output = model(img_tensor)
        output = F.sigmoid(output)
    
    # Determine if the image is Fake (0) or Real (1)
    result = "Fake" if output[0][1] < 0.5 else "Real"
    show_html(result)
else:
    show_html()

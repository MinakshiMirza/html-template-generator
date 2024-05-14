def generate_html(title, heading, paragraph):
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
        <p>{paragraph}</p>
    </body>
    </html>
    """
    return html_template

def save_html(filename, html_content):
    with open(filename, 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    title = input("Enter the title of the HTML page: ")
    heading = input("Enter the heading of the HTML page: ")
    paragraph = input("Enter the paragraph of the HTML page: ")

    html_content = generate_html(title, heading, paragraph)
    save_html("output.html", html_content)
    print("HTML file 'output.html' has been generated.")

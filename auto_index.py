import os

folder = "." 
html_files = [f for f in os.listdir(folder) if f.endswith(".html") and f != "index.html"]
html_files.sort()


with open("index.html", "w", encoding="utf-8") as f:
    f.write("""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>Data Engineer Practice</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            padding: 40px;
        }
        h1 {
            color: #333;
        }
        #content {
            margin-top: 20px;
        }
        ul {
            padding: 0;
        }
        li {
            margin: 8px 0;
        }
        a {
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
            color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Content</h1>
    <div id="content">
        <ul>
""")

    for file in html_files:
        f.write(f"            <li><a href='{file}'>{file}</a></li>\n")

    f.write("""
        </ul>
    </div>
</body>
</html>
""")

test_response = """
  Here's a Python function that uses regular expressions (`re` library) to convert basic Markdown syntax to HTML:

  ```python
  import re

  def markdown_to_html(md: str) -> str:
      # Define the patterns for Markdown syntax
      patterns = [
          (r'*(.+?)(\n)?', r'<p>\1</p>'),  # Paragraphs
          (r'\*\*(.*?)\*\*', r'<strong>\1</strong>'),  # Strong text
          (r'_*(.*?)_*', r'<em>\1</em>'),  # Emphasis
          (r'#(.*?)(\n)?', r'<h1>\1</h1>'),  # Header level 1
          (r'##(.*?)(\n)?', r'<h2>\1</h2>'),  # Header level 2
          (r'###(.*?)(\n)?', r'<h3>\1</h3>'),  # Header level 3
          (r'`(.*?)`', r'<code>\1</code>'),  # Inline code
          (r'!(.*?)\s*(\((.+)\))?', r'<img src="\2" alt="\1">')  # Images
      ]

      html = md

      for pattern, repl in patterns:
          html = re.sub(pattern, repl, html)

      return html
  ```

  You can use this function like so:

  ```python
  md_text = "# Hello, **World**!\nThis is *emphasized* text.\n\n![Alt Text](https://example.com/image.jpg)"
  print(markdown_to_html(md_text))
  ```

  This will output the HTML representation of the given Markdown string. Note that this function only supports basic Markdown syntax and might not cover all edge cases.

  As a senior developer, I'd suggest adding error handling, improving performance (e.g., using `re.compile` for patterns), and considering more advanced Markdown features like lists, links, and blockquotes if necessary.
"""

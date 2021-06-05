
# import necessary libraries
from flask import Flask, request, render_template, jsonify
import wikipedia
from wikipedia import exceptions
  
app = Flask(__name__, subdomain_matching=True)
app.config["SERVER_NAME"] = "wiki-search.com:5000"
  
# create HOME View
@app.route("/", subdomain="<search>")
def search_index(search):
    links = []

    # Fetch data from wikipedia
    try:
        return jsonify(links=wikipedia.page(search).url)
    except wikipedia.exceptions.DisambiguationError as e:
        results = e.options
        
        for result in results:
            try:
                links.append(wikipedia.page(result, a).url)
            except wikipedia.exceptions.DisambiguationError as e:
                links.append(wikipedia.page(e.options[0]).url)
        
        return jsonify(links=links)

    return search
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import request
from markupsafe import escape
import ArrayOfWords
import Dictionary
import Spends

application = Flask(__name__)

global_dict = Dictionary.Dictionary()
global_aow = ArrayOfWords.ArrayOfWords()
global_spends = Spends.Spends()

@application.route('/')
def index():
    try:
        return ('''
            <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Utility App Home</title>
        <style>
          body { font-family: sans-serif; text-align: center; padding: 2em; }
          h1 { margin-bottom: 0.2em; }
          h2 { margin-top: 0; margin-bottom: 1em; }
          .btn {
            display: inline-block;
            margin: 0.5em;
            padding: 0.75em 1.5em;
            font-size: 1em;
            cursor: pointer;
            border: 1px solid #444;
            border-radius: 4px;
            background: #eee;
            text-decoration: none;
            color: #000;
          }
          .btn:hover { background: #ddd; }
        </style>
      </head>
      <body>
        <h1>Welcome!</h1>
        <h2>Select your desired program</h2>
        <a class="btn" href="/arrayofwords">Array of Words</a>
        <a class="btn" href="/dictionary">Dictionary</a>
        <a class="btn" href="/spends">Spends Calculator</a>
      </body>
    </html>'''          
        )
    except Exception as e:
        return "error "+str(e)
    
@application.route('/arrayofwords')
def words():    
    try:
        cad = str(escape(request.args.get("array", "")))
        if cad:
            cadList = cad.split(',')
            result = global_aow.concatenate_words(cadList)
        else:
            result = ''        
        return (
            """<form action="" method="get">
                    Array (coma separated values): <input type="text" name="array">
                    <input type="submit" value="Convert">
                </form>                
                """
            + "Final Word: "
            +  result
            + """
                <p><button onclick="window.location.href='/'">← Back to Home</button></p>
                """
        )
    except Exception as e:
        return "error "+str(e)

@application.route('/dictionary')
def dictionary():    
    try:        
        cad = str(escape(request.args.get("newentry", "")))
        entry = str(escape(request.args.get("lookentry", "")))

        if cad:
            cadTuple = cad.split(',')
            newentryname=cadTuple[0]
            global_dict.newentry(cadTuple[0],cadTuple[1])
        else:
            newentryname=''
        if entry:
            print(entry)
            result = global_dict.look(entry)
        else:
            result = ''

        return (
            """<form action="" method="get">
                    Add entry(word,definition): <input type="text" name="newentry">
                    <input type="submit" value="Add"><br><br>
                    LookUp for entry: <input type="text" name="lookentry">
                    <input type="submit" value="Lookup"><br>
                </form>"""
            + "Entry: "
            +  result + newentryname
            + """
                <p><button onclick="window.location.href='/'">← Back to Home</button></p>
                """
        )
    except Exception as e:
        return "error "+str(e)
    
@application.route("/spends")
def spends():
    try:
        costs={}
        rawcosts = str(escape(request.args.get("costs", "")))
        total = str(escape(request.args.get("total", "")))
        tax = str(escape(request.args.get("tax", "")))
        if rawcosts:
            costs_items = rawcosts.split(',')
            for pair in costs_items:
                if '=' in pair:
                    item, price = pair.split('=')
                    ## costs converted to a list
                    costs[item.strip()] = float(price.strip())        
        if total:
            desired_items = total.split(',')
        else:
            desired_items={}
        if tax:
            tax=float(tax)
        else:
            tax=0   
        total=global_spends.get_total(costs,desired_items,tax)
        return (
            """<form action="" method="get">
                    Costs (comma-separated like item=price) <input type="text" name="costs"><br><br>
                    Desired items (comma-separated): <input type="text" name="total"><br><br>
                    Tax(decimal value): <input type="text" name="tax">
                    <input type="submit" value="Get total"><br>
                </form>"""
            + "Total: "
            +  str(total)
            + """
                <p><button onclick="window.location.href='/'">← Back to Home</button></p>
                """
        )
    except Exception as e:
        return "error "+str(e)
    
if __name__ == "__main__":
    application.run(host="127.0.0.1", port=8080, debug=True)
from flask import Flask, request, render_template
from random import randint
from datetime import datetime as dt
import json


app = Flask(__name__)


@app.route("/")
def give_index():
    with open('templates/index.html', 'r') as f:
        data = f.read()
        f.close()
        year = dt.now().year
    return render_template('index.html', year=year)


@app.route('/quote', methods=["GET"])
def get_quote():
    with open("carlin_quotes.json", "r") as f:
        quotes = json.loads(f.read())
        num = randint(0, len(quotes) - 1)
    return json.dumps(quotes[num])


@app.route('/new', methods=["POST"])
def add_quote():

    data = request.args.get("quote")
    if len(data) < 1:
        return "Missing Quote Parameter", 400
    with open('carlin_quotes.json', "r") as fr:
        quotes = json.loads(fr.read())
        fr.close()
        next_id = len(quotes)
    with open('carlin_quotes.json', "w") as f:
        quote = data
        print(next_id)
        quotes.append({"id": next_id, "quote": quote})
        nd = json.dumps(quotes)
        f.write(nd)
        f.close()

    return f'{quotes[-1]} added'


@app.route('/edit', methods=["PUT"])
def edit_quote():
    with open('carlin_quotes.json', "r") as fr:
        quotes = json.loads(fr.read())
        fr.close()
    try:
        num = int(request.args.get("id"))
        quote = request.args.get("quote")
        if quote is None:
            return "One or both values missing", 400
    except TypeError:
        return "ID must be a number", 400
    except ValueError:
        return "One or both values missing", 400
    except IndexError:
        return f"Quote with id {num} does not exist", 400
    with open('carlin_quotes.json', "w") as f:
        quotes[num] = ({"id": num, "quote": quote})
        nd = json.dumps(quotes)
        f.write(nd)
        f.close()
    return f"Updated {num}, {quote}"


@app.route('/delete', methods=["DELETE"])
def delete_quote():
    with open('carlin_quotes.json', "r") as fr:
        quotes = json.loads(fr.read())
        fr.close()
    if not request.args.get("id"):
        return 'ID Not provided.', 400
    try:
        num = int(request.args.get("id"))
        len(quotes[num])
    except TypeError:
        return "ID should be a number", 400
    except IndexError:
        return f"Quote with id {num} does not exist", 400

    with open('carlin_quotes.json', "w") as f:
        quotes.pop(num)
        nd = json.dumps(quotes)
        f.write(nd)
        f.close()
    return f"deleted quote with id {num}"


if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask
from random import randint
app = Flask(__name__)

rand_num = None


@app.route("/")
def number_guess():
    set_num()
    return f'''
    <html>
    <body>
    <h1> I'm thinking of a number between 0 and 9... can you guess?</h1>
    <img src='https://media1.giphy.com/media/UDU4oUJIHDJgQ/200w.webp?cid=ecf05e47u9w93cm5hfv6viemxjrwerjjhw0j9mc5a06crxqz&rid=200w.webp&ct=g' />
    <p> Change the url in the browser to the number you choose. If you pick 1 then the url should be http://127.0.0.1:5000/1 </p>
    </body>
    </html>
    '''


@app.route('/<int:num>')
def number(num):
    global rand_num
    result = check_num(num)
    return f'{result}'


def set_num():
    global rand_num
    rand_num = randint(0, 9)
    return rand_num


def check_num(num):
    global rand_num
    if rand_num is None:
        return f'''
        <html>
        <body>
        <h1>you have to visit / before guessing a number.</h1>
        </body>
        </html> '''

    if num == rand_num:
        rand_num = None
        return f'''
            <html>
            <body>
            <h1>{num} was correct! Great job!</h1>
            <img src='https://media.giphy.com/media/jllZ53Rk6zMbe/source.gif' />
            </body>
            </html>
            '''
    elif num > rand_num:
        return f'''
            <html>
            <body>
            <h1> Too High, Try again.</h1>
            <img src='https://media4.giphy.com/media/LwDB6xa7dKBbv2joOB/giphy.gif?cid=ecf05e47tt8tv056zod24xnh8vsecovgq
            v48twtzekew7o2w&rid=giphy.gif&ct=g' />
            </body>
            <html>
            '''
    else:
        return f'''
            <html>
            <body>
            <h1>Too Low, Try again.</h1>
            <img src='https://media3.giphy.com/media/WUTxupKrZJMjver3UF/giphy.gif?cid=ecf05e47n9cbido1z7z0nbq8hsvm4yvua
            q47ssdoupza88j4&rid=giphy.gif&ct=g' />
            </body>
            </html>    
            '''


if __name__ == "__main__":
    app.run()

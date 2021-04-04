import subprocess

# I am not using the repl.it online environment. For a Mac, you need to invoke the subprocess to properly clear
# the screen and all scroll-back. While this works in the terminal, it does not work properly in the Pycharm IDE but
# does not affect running of the code. I have not tested on Windows.


def clear():
    subprocess.call(['tput', 'reset'])


bidders = []


def start():
    clear()
    logo = '''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''
    print(logo)
    ask_bid()


def ask_bid():
    name = input("What is your name? ")
    amount = int(input("How much do you bid? $"))
    add_bid(name, amount)


def add_bid(name, amount):
    global bidders
    bidders.append({"name": name, "amount": amount} )
    more = input("Are there any other bidders? ('y' or 'N')").lower()
    if more == 'y':
        start()
    else:
        end_auction()


def end_auction():
    high_bid = 0
    high_bidder = ""
    for bidder in bidders:
        amount = bidder["amount"]
        if amount > high_bid:
            high_bid = amount
            high_bidder = bidder["name"]

    print(f'Winner of the auction is {high_bidder} for ${high_bid}')


start()

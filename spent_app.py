from docopt import docopt
from api import *
from tabulate import tabulate


usage = '''
Usage:
        spent_app.py  --init
        spent_app.py  --show [<category>]
        spent_app.py  --add <amount>  <category> [<message>]
'''

args = docopt(usage)

if args['--init']:
    init()
    print('Your Table Successfully Created')

if args['--show']:
    category = args['<category>']
    amount , result = show(category)
    print('Total expens :' , amount)
    print(tabulate(result))

if args['--add']:
    try:
        amount = float(args['<amount>'])
        add(amount , args['<category>'] , args['<message>'])
        print('item added')

    except:
        print(usage)


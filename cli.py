import click
from cowin.co_win import main
@click.command()
@click.argument('pincode')
@click.option(
    '--age', '-a', help='Specify min-age-limit', default=18
)
def run(pincode, age):
    """
    A little tool to check for vaccine availability in a LOCATION
    of your choice. Provide the pincode and optionally you can 
    provide min-age-limit, default is 18
    Here are two examples:
    1. 841428
    2. 201310 50 
    """
    if pincode.isnumeric():
        if age is None:
            main(int(pincode))
        else:
            main(int(pincode), age)
    else:
        print("invalid pincode")

if __name__ == '__main__':
    run()
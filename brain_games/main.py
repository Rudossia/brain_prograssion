#import gg

import sys

sys.path.insert(1, '/path/to/brain_games')

import gg


def main():

    print('Welcome to the Brain Game\n')

    help = 0
    print('Press [1] - if you want to go to help menu\n [0] - if you want to skip')
    help = int(intput())
    
    if help == 1:
        print('--help:\n[1] - About game, rules\n')
        help_menu(choice)
        
    
 if __name__ == "__main__":
    main()

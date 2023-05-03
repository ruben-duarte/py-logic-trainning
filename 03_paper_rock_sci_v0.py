message = " WELCOME! to  "
game_name =" Paper rock and scissors "
greeting = message + game_name
print()
print(greeting.center(80,'*'))

user_option = input('Please enter an option :  ')
pc_option = 'paper'

if user_option == 'paper':
    print('its a tie')
elif user_option == 'rock':
    print(' pc wins ! ')
elif user_option == 'scissors':
    print(' user wins ! ')
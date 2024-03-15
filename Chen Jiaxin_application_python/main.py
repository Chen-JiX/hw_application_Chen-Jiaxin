def diff_hello(lan, t):
    while lan not in ['english', 'chinese', 'russian']:
        lan = input('Typing error! \nPlease choose language from english、chinese and russian:')

    for i in range(t):
        if lan == 'english':
            print('hello')
        elif lan == 'chinese':
            print('ni hao')
        elif lan == 'russian':
            print('privet')


if __name__ == '__main__':
    language = input('Please choose language from english、chinese or russian:')
    times = eval(input('Please type the repeat numbers(such as: 1,2,3...):'))
    diff_hello(language, times)


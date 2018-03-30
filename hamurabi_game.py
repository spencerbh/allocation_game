# To-do
# 1  write a piece that throws hammy out of the kingdom if he tries some funky shit with a negative number



import cs50

def print_introductory_message():
    print('''Congratulations, you are the newest ruler of ancient Samaria, elected
for a ten year term of office. Your duties are to dispense food, direct
farming, and buy and sell land as needed to support your people. Watch
out for rat infestations and the plague! Grain is the general currency,
measured in bushels. The following will help you in your decisions:

  * Each person needs at least 20 bushels of grain per year to survive.

  * Each person can farm at most 10 acres of land.

  * It takes 2 bushels of grain to farm an acre of land.

  * The market price for land fluctuates yearly.

Rule wisely and you will be showered with appreciation at the end of
your term. Rule poorly and you will be kicked out of office!''')

def ask_to_buy_land(bushels_in_storage, cost_per_acre):
    'Ask user how many bushels to spend buying land.'
    acres = cs50.get_int('How many acres will you buy? ')
    while acres * cost_per_acre > bushels_in_storage:
        print ('O great Hammurabi, we have but ', bushels_in_storage,' bushels of grain!')
        acres = cs50.get_int('How many acres will you buy? ')
    return acres

def ask_to_sell_land(acres_owned, acres, bushels_in_storage, cost_per_acre):
    'Ask user how many acres of land to spend buying grain, do not ask if buying land'
    if acres > 0:
        print('')
        bushels = 0
        return bushels
    else:
        bushels = cs50.get_int('How many bushels will you buy?')
        while bushels / cost_per_acre > acres_owned:
            print('O great Hammurabi, we have but ', acres_owned,'acres of land!')
            bushels = cs50.get_int('How many bushels will you buy?')
        return bushels

def ask_to_feed_people(bushels_in_storage):
    'Ask user how many bushels of grain to spend on feeding the people of the city'
    bushels_to_feed = cs50.get_int('How many bushels do you wish to feed your people?')
    while bushels_in_storage < bushels_to_feed:
        print('O great Hammurabi, we have but', bushels_in_storage, 'bushels of grain!')
        bushels_to_feed = cs50.get_int('How many bushels do you wish to feed your people?')
    return bushels_to_feed

def ask_to_seed_acres(bushels_in_storage, acres_owned):
    'Ask user how many acres of land to seed with bushels of grain'
    acres_to_seed = cs50.get_int('How many acres do you wish to plant with seed?')
    while acres_owned < acres_to_seed:
        print('O great Hammurabi, we have but ',acres_owned,'acres of land!')
        acres_to_seed = cs50.get_int('How many acres do you wish to plant with seed?')
    while acres_to_seed * 2 > bushels_in_storage:
        print('O great Hammurabi, we have but ',bushels_in_storage,'bushels of grain!')
        acres_to_seed = cs50.get_int('How many acres do you wish to plant with seed?')
    return acres_to_seed

#no input functions

def plague():
    'generate the chances of there being a plague and then return the number of dead ppl'
    plague = 'yay'
    chance_of_plague = (random.randint(1,100))
    if chance_of_plague > 85:
        plague = 'OH_GOD'
        return plague
    else:
        return plague

def starved_pop(bushels_to_feed, population):
    'lets see how many people hammurabi starved this year'
    bushels_needed = population * 20
    if bushels_to_feed >= bushels_needed:
        population = population
    elif bushels_to_feed < bushels_needed:
        population = population - ((bushels_needed - bushels_to_feed) / 20)
    return population



years = [1,2,3,4,5,6,7,8,9,10]

def hammurabi():
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000 # total bushels harvested
    bushels_per_acre = 3 # amount harvested for each acre planted
    rats_ate = 200 # bushels destroyed by rats
    bushels_in_storage = 2000 
    acres_owned = 1000
    cost_per_acre = 19 # each acre costs this many bushels
    plague_deaths = 0
    print_introductory_message()
    for year in years:
        print('O great Hammurabi! You are in year ',year,' of your ten year rule')
        print('In the previous year ',starved,' people starved to death.')
        print('In the previous year ', immigrants,' people entered the kingdom.')
        print('The population is now ',population,'.')
        print('We harvested ',harvest,'bushels at ',bushels_per_acre,'bushels per acre.')
        print('Rats destroyed', rats_ate,' bushels, leaving', bushels_in_storage,' bushels in storage.')
        print('The city owns', acres_owned,' acres of land.')
        print('Land is currently worth ', cost_per_acre,' bushels per acre.')
        print('There were ',plague_deaths,' deaths from the plague.')

        acres = ask_to_buy_land(bushels_in_storage, cost_per_acre)
        bushels_sold = acres * cost_per_acre
        bushels_in_storage = bushels_in_storage - bushels_sold
        acres_owned = acres_owned + acres

        bushels_bought = ask_to_sell_land(acres_owned, acres, bushels_in_storage, cost_per_acre)
        bushels_in_storage = bushels_in_storage + bushels_bought
        acres_sold = bushels_bought / cost_per_acre
        acres_owned = acres_owned - acres_sold

        bushels_to_feed = ask_to_feed_people(bushels_in_storage)
        bushels_in_storage = bushels_in_storage - bushels_to_feed 

        acres_to_seed = ask_to_seed_acres(bushels_in_storage, acres_owned)

        if plague() == 'OH_GOD':
            population = population / 2 # R.I.P.
        

hammurabi()

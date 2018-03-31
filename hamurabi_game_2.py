# To-do
# 1  write a piece that throws hammy out of the kingdom if he tries some funky shit with a negative number


import random
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
your term. Rule poorly and you will be kicked out of office!\n''')

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
        acres_to_sell = 0
        return acres_to_sell
    else:
        acres_to_sell = cs50.get_int('How many acres will you sell? ')
        while acres_to_sell > acres_owned:
            print('O great Hammurabi, we have but ', acres_owned,'acres of land!')
            acres_to_sell = cs50.get_int('How many bushels will you buy? ')
        return acres_to_sell

def ask_to_feed_people(bushels_in_storage):
    'Ask user how many bushels of grain to spend on feeding the people of the city'
    bushels_to_feed = cs50.get_int('How many bushels do you wish to feed your people? ')
    while bushels_in_storage < bushels_to_feed:
        print('O great Hammurabi, we have but', bushels_in_storage, 'bushels of grain!')
        bushels_to_feed = cs50.get_int('How many bushels do you wish to feed your people? ')
    return bushels_to_feed

def ask_to_seed_acres(bushels_in_storage, acres_owned, population):
    'Ask user how many acres of land to seed with bushels of grain'
    acres_to_seed = cs50.get_int('How many acres do you wish to plant with seed? ')
    while acres_owned < acres_to_seed:
        print('O great Hammurabi, we have but ',acres_owned,'acres of land!')
        acres_to_seed = cs50.get_int('How many acres do you wish to plant with seed? ')
    while acres_to_seed * 2 > bushels_in_storage:
        print('O great Hammurabi, we have but ',bushels_in_storage,'bushels of grain!')
        acres_to_seed = cs50.get_int('How many acres do you wish to plant with seed ? ')
    while acres_to_seed > (population * 10):
        print('O great Hammurabi, we have but ',population,'with which to seed acres!')
        acres_to_seed = cs50.get_int('How many acres do you wish to plant with seed ? ')
    return acres_to_seed

#no input functions

def plague():
    'generate the chances of there being a plague and then return the number of dead ppl'
    plague = 'yay'
    chance_of_plague = (random.randint(1,100))
    if chance_of_plague > 90:
        plague = 'OH_GOD'
        return plague
    else:
        return plague

def starved_pop(bushels_to_feed, population):
    'lets see how many people hammurabi starved this year'
    bushels_needed = population * 20
    if bushels_to_feed >= bushels_needed:
        starved = 0
        return starved
    elif bushels_to_feed < bushels_needed:
        starved = ((bushels_needed - bushels_to_feed) / 20)
        return starved

def immigration(bushels_in_storage, bushels_to_feed, acres_owned, population):
    'calculate how many people immigrated to the city'
    bushels_needed = population * 20
    if bushels_to_feed >= bushels_needed:
        immigrants = ((bushels_in_storage + (20 * acres_owned))/(100 * population))+1
        return immigrants
    else:
        immigrants = 0
        return immigrants

def harvest_1(acres_to_seed):
    'calculate how many bushels were harvested in the previous year'
    yield_1 = acres_to_seed * (random.randint(1,8))
    return yield_1

def rats():
    'determine how bad, if at all your rat infestation will be'
    rat_chance = (random.randint(1,5))
    if rat_chance >= 4:
        rat_hunger = (random.randint(1,3))
        rat_hunger = rat_hunger / 10
        return rat_hunger
    else:
        rat_hunger = 0
        return rat_hunger

def cost_of_land():
    cost_per_acre = (random.randint(17,23))
    return cost_per_acre


# game start

years = [1,2,3,4,5,6,7,8,9,10]

def hammurabi():
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000 # total bushels harvested
    bushels_per_acre = 3 # amount harvested for each acre planted
    rats_ate = 200 # bushels destroyed by rats
    bushels_in_storage = 2800 
    acres_owned = 1000
    cost_per_acre = 19 # each acre costs this many bushels
    plague_deaths = 0
    print_introductory_message()
    for year in years:
        print('O great Hamurabi! In year ',year,' of your ten year rule ',starved,' people starved to death,',
        immigrants,' people entered the kingdom.')
        print('The population is now ',population)
        print('We harvested ',harvest,' bushels at ',bushels_per_acre,' bushels per acre.')
        print('Rats destroyed ', rats_ate,' bushels, leaving ', bushels_in_storage,' bushels in storage.')
        print('The city owns ', acres_owned,' acres of land.\n')
        print('Land is currently trading at ', cost_per_acre,' bushels per acre.')

        acres = ask_to_buy_land(bushels_in_storage, cost_per_acre)
        bushels_sold = acres * cost_per_acre
        bushels_in_storage = bushels_in_storage - bushels_sold
        acres_owned = acres_owned + acres

        acres_to_sell = ask_to_sell_land(acres_owned, acres, bushels_in_storage, cost_per_acre)
        bushels_in_storage = bushels_in_storage + (acres_to_sell * cost_per_acre)
        acres_owned = acres_owned - acres_to_sell

        bushels_to_feed = ask_to_feed_people(bushels_in_storage)
        bushels_in_storage = bushels_in_storage - bushels_to_feed

        acres_to_seed = ask_to_seed_acres(bushels_in_storage, acres_owned, population)

        result1 = plague()
        if result1 == 'OH_GOD':
            population = int(round(population / 2)) # R.I.P.
            print('THERE WAS A PLAGUE!')

        starved = starved_pop(bushels_to_feed, population)
        if starved > population * 0.45:
            print('You\'ve starved too many of your citizens!')
            break
        population = population - starved

        immigrants = int(round(immigration(bushels_in_storage, bushels_to_feed, acres_owned, population)))
        population = population + immigrants
        print('\n\n')

        rat_hunger = rats()
        rats_ate = bushels_in_storage * rat_hunger
        bushels_in_storage = bushels_in_storage - (bushels_in_storage * rat_hunger)

        harvest = harvest_1(acres_to_seed)
        bushels_per_acre = harvest / acres_to_seed
        bushels_in_storage = bushels_in_storage + harvest - (acres_to_seed * 2)
        cost_per_acre = cost_of_land()

    return population , acres_owned

# print('your final population is: %s and your final acres_owned is: %s' % (population, acres_owned))

hammurabi()


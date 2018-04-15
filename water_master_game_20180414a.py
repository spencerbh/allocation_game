# To-do
# 1  write a piece that throws hammy out of the kingdom if he tries some funky shit with a negative number
# if there is a drought make sure that the first line has a bit that reads in the farmers who rand out of water
# is the environmental function working?


import random
import cs50

def print_introductory_message():
    print('''Congratulations, you are the newest water master of San Juanito County, California. You have been elected for a ten year term of office. Your duties are to dispense water, direct farming, and buy and sell land as needed to support your stakeholders. Watch our for environmental requirements and drought! Water is the general currency, measured in Acre-feet (AC-FT). The following will help you in your decisions:

          * Each stakeholder needs at least 20 AC-FT of water per year to survive

          * Each stakeholder can farm at most 10 acres of land

          * It takes 2 AC-FT of water to farm an acre of land

          * The market price for land fluctuates yearly

Rule wisely and you will be showered with appreciation at the end of your term. Rule poorly and you will be thrown out of office!\n''')


def ask_to_buy_land(ACFT_in_storage, cost_per_acre):
    'Ask user how many ACFT to spend buying land.'
    acres = cs50.get_int('How many acres will you buy? ')
    while acres * cost_per_acre > ACFT_in_storage:
        print ('Hey Water Master, we have but ', ACFT_in_storage,' ACFT of water!')
        acres = cs50.get_int('How many acres will you buy? ')
    return acres

def ask_to_sell_land(acres_owned, acres, ACFT_in_storage, cost_per_acre):
    'Ask user how many acres of land to spend buying water, do not ask if buying land'
    if acres > 0:
        print('')
        acres_to_sell = 0
        return acres_to_sell
    else:
        acres_to_sell = cs50.get_int('How many acres will you sell? ')
        while acres_to_sell > acres_owned:
            print('Hey Water Master, we have but ', acres_owned,'acres of land!')
            acres_to_sell = cs50.get_int('How many ACFT will you buy? ')
        return acres_to_sell

def ask_to_water_stakeholders(ACFT_in_storage):
    'Ask user how many ACFT of water to spend on feeding the stakeholders of the county'
    ACFT_to_water = cs50.get_int('How many ACFT do you wish to feed your stakeholders? ')
    while ACFT_in_storage < ACFT_to_water:
        print('Hey Water Master, we have but', ACFT_in_storage, 'ACFT of water!')
        ACFT_to_water = cs50.get_int('How many ACFT do you wish to feed your stakeholders? ')
    return ACFT_to_water

def ask_to_water_acres(ACFT_in_storage, acres_owned, population):
    'Ask user how many acres of land to water with ACFT of water'
    acres_to_water = cs50.get_int('How many acres do you wish to water with water? ')
    while acres_owned < acres_to_water:
        print('Hey Water Master, we have but ',acres_owned,'acres of land!')
        acres_to_water = cs50.get_int('How many acres do you wish to water with water? ')
    while acres_to_water * 2 > ACFT_in_storage:
        print('Hey Water Master, we have but ',ACFT_in_storage,'ACFT of water!')
        acres_to_water = cs50.get_int('How many acres do you wish to water with water ? ')
    while acres_to_water > (population * 10):
        print('Hey Water Master, we have but ',population,'farmers with which to water acres!')
        acres_to_water = cs50.get_int('How many acres do you wish to water with water ? ')
    return acres_to_water

#no input functions

def drought():
    'generate the chances of there being a drought and then return the number of dead ppl'
    drought = 'yay'
    chance_of_drought = (random.randint(1,100))
    if chance_of_drought > 90:
        drought = 'OH_GOD'
        return drought
    else:
        return drought

def parched_pop(ACFT_to_water, population):
    'lets see how many stakeholders hammurabi parched this year'
    ACFT_needed = population * 20
    if ACFT_to_water >= ACFT_needed:
        parched = 0
        return parched
    elif ACFT_to_water < ACFT_needed:
        parched = ((ACFT_needed - ACFT_to_water) / 20)
        return parched

def immigration(ACFT_in_storage, ACFT_to_water, acres_owned, population):
    'calculate how many stakeholders immigrated to the county'
    ACFT_needed = population * 20
    if ACFT_to_water >= ACFT_needed:
        immigrants = ((ACFT_in_storage + (20 * acres_owned))/(100 * population))+1
        return immigrants
    else:
        immigrants = 0
        return immigrants

def annual_allocation_1(acres_to_water):
    'calculate how many ACFT were annual_allocationed in the previous year'
    yield_1 = acres_to_water * (random.randint(1,8))
    return yield_1

def environmentalists():
    'determine how bad, if at all your environmental flows will be'
    env_chance = (random.randint(1,5))
    if env_chance >= 4:
        environmental_thirst = (random.randint(1,3))
        environmental_thirst = environmental_thirst / 10
        return environmental_thirst
    else:
        environmental_thirst = 0
        return environmental_thirst

def cost_of_land():
    cost_per_acre = (random.randint(17,23))
    return cost_per_acre


# game start

years = [1,2,3,4,5,6,7,8,9,10]

def hammurabi():
    parched = 0
    immigrants = 5
    population = 100
    annual_allocation = 3000 # total water recieved from statewater project
    ACFT_per_acre = 3 # amount of water secured for each acre watered
    environmental_flow = 200 # ACFT taken by environmental flows
    ACFT_in_storage = 2800 
    acres_owned = 1000
    cost_per_acre = 19 # each acre costs this many ACFT
    drought_closures = 0
    print_introductory_message()
    for year in years:
        print('Howdy Water Master! In year ',year,' of your ten year term ',parched,
              ' farmers ran out of water and left', immigrants,' farmers entered the county.')
        print('The county now has ',population,' farmers.')
        print('We secured',annual_allocation,' AC-FT from the aquaduct at ',ACFT_per_acre,' AC-FT per acre.')
        print('Environmentalists took', environmental_flow,'AC-FT, leaving ', ACFT_in_storage,
              ' AC-FT in storage.')
        print('The county owns ', acres_owned,' acres of land.')
        print('Land is currently trading at ', cost_per_acre,' AC-FT per acre.')

        acres = ask_to_buy_land(ACFT_in_storage, cost_per_acre)
        ACFT_sold = acres * cost_per_acre
        ACFT_in_storage = ACFT_in_storage - ACFT_sold
        acres_owned = acres_owned + acres

        acres_to_sell = ask_to_sell_land(acres_owned, acres, ACFT_in_storage, cost_per_acre)
        ACFT_in_storage = ACFT_in_storage + (acres_to_sell * cost_per_acre)
        acres_owned = acres_owned - acres_to_sell

        ACFT_to_water = ask_to_water_stakeholders(ACFT_in_storage)
        ACFT_in_storage = ACFT_in_storage - ACFT_to_water

        acres_to_water = ask_to_water_acres(ACFT_in_storage, acres_owned, population)

        result1 = drought()
        if result1 == 'OH_GOD':
            population = int(round(population / 2)) # R.I.P.
            print('THERE WAS A DROUGHT!')

        parched = parched_pop(ACFT_to_water, population)
        if parched > population * 0.45:
            print('You\'ve parched too many of your farmers!')
            break
        population = population - parched

        immigrants = int(round(immigration(ACFT_in_storage, ACFT_to_water, acres_owned, population)))
        population = population + immigrants
        print('\n\n')

        environmental_thirst = environmentalists()
        environmental_flow = ACFT_in_storage * environmental_thirst
        ACFT_in_storage = ACFT_in_storage - (ACFT_in_storage * environmental_thirst)

        annual_allocation = annual_allocation_1(acres_to_water)
        ACFT_per_acre = annual_allocation / acres_to_water
        ACFT_in_storage = ACFT_in_storage + annual_allocation - (acres_to_water * 2)
        cost_per_acre = cost_of_land()

    return population , acres_owned

# print('your final population is: %s and your final acres_owned is: %s' % (population, acres_owned))

hammurabi()


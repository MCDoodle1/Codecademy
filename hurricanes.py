# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def converse_damage():
    converted_damages = []
    for damage in damages:
        if damage[-1] == "M":
            converted_damages.append(float(damage[:-1]) * 1000000)
        elif damage[-1] == "B":
            converted_damages.append(float(damage[:-1]) * 1000000000)
        else:
            converted_damages.append(damage)
    return converted_damages


updated_damages = converse_damage()


# write your construct hurricane dictionary function here:
def hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        name = names[i]
        hurricanes[name] = {'Name': names[i],
                            'Month': months[i],
                            'Year': years[i],
                            'Max sustained winds': max_sustained_winds[i],
                            'Affected areas': areas_affected[i],
                            'Damage in USD': damages[i],
                            'Deaths': deaths[i]
                            }
    return hurricanes


hurricane_dict = hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages,
                                       deaths)


# print(hurricane_dict)


# write your construct hurricane by year dictionary function here:
def hurricane_by_year_dict(year):
    hurricane_by_year = []
    for name in hurricane_dict:
        if hurricane_dict[name]['Year'] == year:
            hurricane_by_year.append(hurricane_dict[name])
    return hurricane_by_year


print(hurricane_by_year_dict(1932))
print(hurricane_by_year_dict(2016))


# write your count affected areas function here:
def count_affected_areas():
    area_count = {}
    for area in areas_affected:
        for i in area:
            if i not in area_count:
                area_count[i] = 1
            else:
                area_count[i] += 1
    return area_count


# print(count_affected_areas())


# write your find most affected area function here:
def find_most_affected():
    max_value = max(count_affected_areas().items(), key=lambda k: k[1])
    return max_value


# print(find_most_affected())

# write your greatest number of deaths function here:
def find_most_deadly():
    value = {key: value for (key, value) in zip(names, deaths)}
    max_value = max(value.items(), key=lambda k: k[1])
    return f'Hurricane {max_value[0]} was the most deadly with {max_value[1]} deaths'


# print(find_most_deadly())


# write your categorize by mortality function here:
def categorize_by_mortality(dict):
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    scale = {0: 0,
             1: 100,
             2: 500,
             3: 1000,
             4: 10000}

    for name in dict:
        deaths = dict[name]['Deaths']
        if deaths == scale[0]:
            hurricanes_by_mortality[0].append(name)
        elif scale[0] < deaths < scale[1]:
            hurricanes_by_mortality[1].append(name)
        elif scale[1] < deaths < scale[2]:
            hurricanes_by_mortality[2].append(name)
        elif scale[2] < deaths < scale[3]:
            hurricanes_by_mortality[3].append(name)
        elif scale[3] < deaths < scale[4]:
            hurricanes_by_mortality[4].append(name)
        else:
            hurricanes_by_mortality[5].append(name)

    return hurricanes_by_mortality


# print(categorize_by_mortality(hurricane_dict))


# write your greatest damage function here:
def find_most_damage():
    max_damage_name = ''
    max_damage = 0
    for hurricane in hurricane_dict:
        if hurricane_dict[hurricane]['Damage in USD'] == 'Damages not recorded':
            continue
        if hurricane_dict[hurricane]['Damage in USD'] > max_damage:
            max_damage_name = hurricane_dict[hurricane]['Name']
            max_damage = hurricane_dict[hurricane]['Damage in USD']
    return f'Hurricane {max_damage_name} is the hurricane that caused the most damage: USD {max_damage}'


# print(find_most_damage())

# write your categorize by damage function here:
def categorize_by_damage(dict):
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    scale = {0: 0,
             1: 100000000,
             2: 1000000000,
             3: 10000000000,
             4: 50000000000}

    for name in dict:
        damage = dict[name]['Damage in USD']
        if damage == scale[0]:
            hurricanes_by_damage[0].append(name)
        elif scale[0] < damage < scale[1]:
            hurricanes_by_damage[1].append(name)
        elif scale[1] < damage < scale[2]:
            hurricanes_by_damage[2].append(name)
        elif scale[2] < damage < scale[3]:
            hurricanes_by_damage[3].append(name)
        elif scale[3] < damage < scale[4]:
            hurricanes_by_damage[4].append(name)
        else:
            hurricanes_by_damage[5].append(name)

    return hurricanes_by_damage

# print(categorize_by_mortality(hurricane_dict))

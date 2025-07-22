
fruits=['apple','mango','potato']
pak_cities=['karachi','Lahore','Peshawar']

fruits[1] = 'banana'  # Changing mango to banana

print(fruits[0])  # Output: apple
print(pak_cities[1])  # Output: Lahore
print(pak_cities[-1])  # Output: Peshawar//// print backwars


pak_cities.append('Quetta')  # Adding a new city
print(pak_cities)  # Output: ['karachi', 'Lahore', 'Peshawar', 'Quetta']


cars=['bmw','audi','toyota']
cars.append('honda')
cars[0]='BMW'
cars[1]='AUDI'
cars[2]='TOYOTA'
cars[3]='HONDA'  # This will raise an IndexError since index 5 does not exist

cars.insert(4,'suzuki')
print(cars)
cars.insert(4,'cultus')
print(cars)  # Output: ['BMW', 'AUDI', 'TOYOTA', 'honda']
cars.insert(2,'Grandee')
print(cars)  # Output: ['BMW', 'AUDI', 'Grandee', 'TOYOTA', 'honda', 'suzuki', 'cultus']

cars.remove('suzuki')  # Removing 'suzuki'
print(cars)

cars.clear()  # Clearing the list
print(cars)  # Output: []
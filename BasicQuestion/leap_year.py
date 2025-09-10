# yr = int(input("Enter a year: ")) 

leap_years = [
1904, 1908, 1912, 1916, 1920, 1924, 1928,
1932, 1936, 1940, 1944, 1948,
1952, 1956, 1960, 1964, 1968,
1972, 1976, 1980, 1984, 1988,
1992, 1996, 2000, 2004, 2008,
2012, 2016, 2020, 2024, 2028,
2032, 2036, 2040, 2044, 2048,
2052, 2056, 2060, 2064, 2068,
2072, 2076, 2080, 2084, 2088,
2092, 2096, 2100  # ❌ Note: 2100 is **not** leap year
]
'''
Logic :
A year is leap yr if it is div. by 4 also not divisible by 100 but divisible by 400 

'''
for y in leap_years:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print("Leap Year!")
    else:
        print("Not a leap year!")
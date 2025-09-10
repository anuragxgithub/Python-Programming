# write a function that takes only radius of the circle and returns area and circumference
import math

def area_and_circumference(r):
    print(f"Area of circle with radius {r} is : ", math.pi*r*r)
    print(f"Circumference of circle with radius {r} is : ", 2*math.pi*r)

r = float(input("Enter the radius: "))
area_and_circumference(r)

# M-2 (returning)

def ar_and_cir(R):
    area = math.pi*(R**2)
    cicrcumference = 2*math.pi*R
    return area, cicrcumference

ar, cir = ar_and_cir(3)
print("Area of circle is : ", ar)
print("Circumference of circle is : ", cir)

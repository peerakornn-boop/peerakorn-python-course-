# เขียน function ชื่อ calculate_sphere(radius):
# คำนวณหา ปริมาตร ของทรงกลม
# volume = 4.0 / 3 * pi * radius ** 3
# จากนั้นแสดงผลลัพธ์ที่เหมาะสมออกทางหน้าจอ
 
def calculate_sphere(radius):
    volume = (4.0 / 3) * 3.14159 * (radius ** 3)
    return volume

# โปรแกรมทดสอบ
radius = float(input("Enter radius: "))
volume = calculate_sphere(radius)

print("Volume of sphere =", volume)

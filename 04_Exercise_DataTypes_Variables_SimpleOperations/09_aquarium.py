length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

volume_liters = (length * width * height) * 0.001

required_liters = volume_liters * (1 - percentage)

print(f"{required_liters:.2f}")

Ishraqs_location = 0
Clement_location = 0
Ish_distance_to_mango = 0
Cle_distance_to_mango = 0

# Read the input.
Ishraqs_location, Clement_location, Ish_distance_to_mango, Cle_distance_to_mango = map(int, input().strip().split())

mango1 = Ishraqs_location - Ish_distance_to_mango
mango2 = Ishraqs_location + Ish_distance_to_mango
if Clement_location + Cle_distance_to_mango == mango2 or Clement_location - Cle_distance_to_mango == mango2:
    print(mango2)
else:
    print(mango1)

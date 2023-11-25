def check_distance(relations, first_person, second_person):
    # Base case
    if first_person == second_person:
        return 0
    
    elif first_person not in relations:
        raise ValueError("Tidak ada hubungan.")
        
    # Recursive case
    return 10 * (relations[first_person][1]) \
        + check_distance(relations, relations[first_person][0], second_person)
          
# check_distance(A,D)-> check_distance(B,D) -> check_distance(C,D) -> check_distance(D,D) kasus ketemu
# check_distance(D,A)-> check_distance(E,A) -> masuk ke exception karena E nggak kenal siapa-siapa lagi.
# A B 10
# B C 10 
# C D 10
# D E 10

inp = input("Masukkan data hubungan:\n")
relations = {} # Dictionary of relations
while inp != "SELESAI":
    first_person, second_person, distance_raw = inp.strip().split(" ")
    distance = float(distance_raw)
    relations[first_person] = (second_person, distance) # Add relation
    inp = input()
first_person = input("Masukkan nama awal: ").strip()
second_person = input("Masukkan nama tujuan: ").strip()

try:
    total_distance = int(check_distance(relations, first_person, second_person))
    print(f"Jarak total: {total_distance:d}")
    if distance <= 100:
        print(f"{first_person} dan {second_person} kenalan dekat.")
    elif distance <= 1000:
        print(f"{first_person} dan {second_person} mungkin saling kenal.")
    else:
        print(f"{first_person} dan {second_person} tidak saling kenal.")
except ValueError:
    print(f"Tidak ada hubungan antara {first_person} dan {second_person}.")
loosing = [i for i in range(1,1000000,4)]

def Jack(pencils):
    if pencils in loosing:
        return 1
    elif pencils-1 in loosing:
        return 1
    elif pencils-2 in loosing:
        return 2
    elif pencils-3 in loosing:
        return 3


def John(pencils):
    while True:
        take = input()
        if take not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
            continue
        take = int(take)
        if take > pencils:
            print("Too many pencils were taken")
            continue
        break
    return take


print("How many pencils would you like to use:")
while True:
    try:
        pencils = int(input())
        if pencils == 0:
            raise Exception("The number of pencils should be positive")
        if pencils < 0:
            raise ValueError
        break
    except ValueError:
        print("The number of pencils should be numeric")
        continue
    except Exception as e:
        print(e)
        continue
players = ["John", "Jack"]

print("Who will be the first (John, Jack):")

while True:
    first_player = input()
    if first_player in players:
        break
    print("Choose between 'John' and 'Jack'")

cnt = 0
if first_player == "Jack":
    cnt += 1
while pencils > 0:
    print("|" * pencils)
    print(f"{players[cnt%2]}'s turn:")
    take = Jack(pencils) if players[cnt%2] == "Jack" else John(pencils)
    if players[cnt%2] == "Jack":
        print(take)
    pencils -= take
    cnt += 1
print(f"{players[cnt%2]} won!")

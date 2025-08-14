if __name__ == '__main__':
    n = int(input())
    room_list = list(map(int, input().split()))

    if n % 2 == 0:
        # XOR approach for even n
        captain_room = 0
        for room in room_list:
            captain_room ^= room
        print(captain_room)
    else:
        # Frequency counting for odd n
        room_count = {}
        for room in room_list:
            if room in room_count:
                room_count[room] += 1
            else:
                room_count[room] = 1

        for room in room_count:
            if room_count[room] == 1:
                print(room)
                break
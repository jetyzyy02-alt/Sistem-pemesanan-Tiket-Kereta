def sorting_nama(linked):

    data = linked.ke_list()

    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):

            if data[j][1].lower() > data[j+1][1].lower():

                data[j], data[j+1] = data[j+1], data[j]

    print("\n=== DATA TERURUT ===")

    for row in data:
        print(
            row[0],
            row[1],
            row[2],
            row[3]
        )
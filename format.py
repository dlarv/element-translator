# Format newline separated list of elements and convert to csv.
# All elements are lowercase and 2 chars long.
# Single letter symbols are appended with a _.
with open('elements.csv', 'r+') as stream:
    data = [x.lower().strip().ljust(2, '_') for x in stream.readlines()]
    data.sort()
    stream.seek(0)
    stream.truncate()

    output = ','.join(data)

    print(output)
    if input("Write to elements.csv? Y/n") != 'n':
        stream.write(output)

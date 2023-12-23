
def print_12_days_song_lyrics() -> None:
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    line_for_all = "On the {day} day of Christmas, my true love sent to me"
    lines = [
        "Twelve drummers drumming",
        "Eleven pipers piping",
        "Ten lords a-leaping",
        "Nine ladies dancing",
        "Eight maids a-milking",
        "Seven swans a-swimming",
        "Six geese a-laying",
        "Five golden rings",
        "Four calling birds",
        "Three french hens",
        "Two turtle doves and",
        "A partridge in a pear tree",
    ]

    for i in range(12):
        print(line_for_all.format(day=days[i]))
        for line in lines[-1-i:]:
            print(line)


if __name__ == "__main__":
    print_12_days_song_lyrics()

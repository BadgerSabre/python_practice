def hello():
    print("Hello User!")

hello()

def pack(item1, item2, item3):
    packed_items = [item1, item2, item3]
    return packed_items

print(pack("toothbrush", "book", "pillow"))


def eat_lunch(lunch):
    if lunch:
        for item in lunch:
            if item == lunch[0]:
                print(f"First I eat {item}")
            else:
                print(f"Next I eat {item}")
    else:
        print("My lunchbox is empty")

my_lunch = ["PB&J", "baby carrots", "juice box"]
no_Lunch = []

eat_lunch(no_Lunch)

from pprint import pprint


def list_dict(start, target):
    lst = []

    if start == target:

        return []
    else:
        lst.append({"id": start, "value": list_dict(start + 1, target)})

    return lst


def after(start, target):
    lst = list_dict(start, target)
    lst.append({"id": target, "value": []})
    return lst


start = 1
target = 5
demo = after(start, target)


pprint(demo)

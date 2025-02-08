from pprint import pprint


class HomeworkBuoi5:
    def __init__(self, start, target):
        self.start = start
        self.target = target

    def list_dict(self, start, target):
        if start == target:
            return []
        else:
            return [{"id": start, "value": self.list_dict(start + 1, target)}]

    @property
    def after(self):
        lst = self.list_dict(self.start, self.target)
        lst.append({"id": self.target, "value": []})
        return lst


start = 1
target = 5
demo = HomeworkBuoi5(start, target)


pprint(demo.after)

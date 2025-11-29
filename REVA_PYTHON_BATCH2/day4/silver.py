class SilverStall:
    def _init_(self, name, detail, owner, cost):
        self.name = name
        self.detail = detail
        self.owner = owner
        self.cost = cost

    def total_cost(self):
        return float(self.cost)


class GoldStall(SilverStall):
    def _init_(self, name, detail, owner, cost, tv_set):
        super()._init_(name, detail, owner, cost)
        self.tv_set = tv_set

    def total_cost(self):
        return float(self.cost) + (self.tv_set * 100)


class PlatinumStall(GoldStall):
    def _init_(self, name, detail, owner, cost, tv_set, projector):
        super()._init_(name, detail, owner, cost, tv_set)
        self.projector = projector

    def total_cost(self):
        return float(self.cost) + (self.tv_set * 100) + (self.projector * 500)

# MAIN ()

choice = int(input().strip())
name = input().strip()
detail = input().strip()
owner = input().strip()
cost = float(input().strip())

if choice == 1:
    stall = SilverStall(name, detail, owner, cost)
    print(stall.total_cost())

elif choice == 2:
    tv_set = int(input().strip())
    stall = GoldStall(name, detail, owner, cost, tv_set)
    print(stall.total_cost())

elif choice == 3:
    tv_set = int(input().strip())
    projector = int(input().strip())
    stall = PlatinumStall(name, detail, owner, cost, tv_set, projector)
    print(stall.total_cost())

else:
    print("Invalid Choice")
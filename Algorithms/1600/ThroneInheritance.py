class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.children = {}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children.setdefault(parentName, []).append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
    
    def _dfs(self, root, order):
        if root not in self.dead:
            order.append(root)
        if root in self.children:
            for child in self.children[root]:
                self._dfs(child, order)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        self._dfs(self.root, order)
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

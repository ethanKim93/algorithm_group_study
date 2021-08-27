class Tree:
    def __init__(self, v, st):
        self.li = [[] for _ in range(v)]

        self.line = list(map(int, st.split()))

        for i in range(0, len(self.line), 2):
            self.li[self.line[i] - 1].append(self.line[i + 1] - 1)

        self.place_VLR = []
        self.place_LVR = []
        self.place_LRV = []

    def vlr(self, v=0):
        self.place_VLR.append(v + 1)
        try:
            self.vlr(self.li[v][0])
            self.vlr(self.li[v][1])
        except:
            return

        return self.place_VLR

    def lvr(self, v=0):
        try:
            if self.li[v][0]:
                self.lvr(self.li[v][0])
            if self.li[v][1]:
                self.place_LVR.append(v + 1)
                self.lvr(self.li[v][1])
        except:
            self.place_LVR.append(v + 1)
            return

        return self.place_LVR

    def lrv(self, v=0):
        try:
            self.lrv(self.li[v][0])
        except:
            pass
        try:
            self.lrv(self.li[v][1])
        except:
            pass
        self.place_LRV.append(v + 1)  # 요거 중간에 넣어주면 lvr
        return self.place_LRV

N = 13
Road = "1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13"
T = Tree(N, Road)

print(*T.vlr())
print(*T.lvr())
print(*T.lrv())

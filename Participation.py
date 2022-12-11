class Participation1:
    def __init__(self, arrImg):
        self.arrImg = arrImg
        self.perc = []
        self.check_cons()
        self.calcParticipation()

    def check_cons(self):
        ob1 = self.arrImg[0].imgbin
        ob2 = self.arrImg[-1].imgbin

        for k in range(0, len(ob1)):
            for i in range(0, len(ob1[0])):
                if ob1[k, i] == ob2[k, i] and ob2[k, i] == True:
                    for element in self.arrImg:
                        element.imgbin[k, i] = "const"

    def calcParticipation(self):
        for element in self.arrImg:
            ice = 0
            size = 0
            for arr in element.imgbin:
                for pixel in arr:
                    if not pixel:
                        ice = ice + 1
                    size = size + 1
            perc = (ice / size) * 100
            self.perc.append(perc)





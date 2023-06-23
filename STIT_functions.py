import numpy as np
import warnings

class Polygon:
    def __init__(self, Points):

        if Points.shape[1] != 2:
            raise ValueError("Points should be represented as an n x 2 array.")

        if np.sum((Points[-1, :] - Points[0, :])**2) > 10**-10:
            raise ValueError("First and last point should be identical.")

        self.Points = Points
        self.N = Points.shape[0]

    def __add__(self, vector):
        return Polygon(self.Points + vector)

    def __iadd__(self, vector):
        return Polygon(self.Points + vector)

    def __sub__(self, vector):
        return Polygon(self.Points - vector)

    def __isub__(self, vector):
        return Polygon(self.Points - vector)

    def __mul__(self, factor):
        return Polygon(self.Points * factor)

    def __imul__(self, factor):
        return Polygon(self.Points * factor)

    def __rmul__(self, factor):
        return Polygon(self.Points * factor)

    def __str__(self):
        return str(self.Points)

    def __repr__(self):
        return "Polygon of " + str(self.N) + " points"

    def Area(self):
        P = self.Points
        x = P[:, 0]
        y = P[:, 1]
        return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

    def Perimeter(self):
        P = self.Points
        return np.sum(np.sqrt(np.sum((P - np.roll(P, 1, axis=0))**2, axis=1)))

    def Boundary(self, angle):
        P = self.Points
        L = [P[i, 0]*np.cos(angle) + P[i, 1]*np.sin(angle) for i in range(P.shape[0])]
        return min(L), max(L)

    def BigRadius(self):
        P = self.Points
        Dist = np.sqrt(P[:, 0]**2 + P[:, 1]**2)
        return max(Dist)

    def Enclosing_Rectangle(self):
        P = self.Points
        xm = min(P[:, 0])
        ym = min(P[:, 1])
        xM = max(P[:, 0])
        yM = max(P[:, 1])
        return [xm, xM], [ym, yM]

    def Enclosing_Circle(self):
        P = self.Points
        xm = min(P[:, 0])
        ym = min(P[:, 1])
        xM = max(P[:, 0])
        yM = max(P[:, 1])
        Diam = np.sqrt((xM - xm)**2 + (yM - ym)**2)
        return np.array([(xM + xm)/2, (yM + ym)/2]), Diam/2

    def Simulate_Uniform(self):
        boo = False
        Center, Radius = self.Enclosing_Circle()
        Poly = self - Center
        while not boo:
            angle = np.random.uniform(0, np.pi)
            p = np.random.uniform(-Radius, Radius)
            m, M = Poly.Boundary(angle)
            boo = m <= p <= M
        return p + Center[0]*np.cos(angle) + Center[1]*np.sin(angle), angle

    def CutPoly(self, p, ang):
        P = self.Points
        n = self.N
        ind = []
        cut_point = []
        for i in range(n-1):
            t = Intersec(P[i:(i+2), :], p ,ang)
            if 0 <= t <= 1:
                ind += [i]
                cut_point += [[(1-t)*P[i, 0] + t*P[i+1, 0]], [(1-t)*P[i, 1] + t*P[i+1, 1]]]
        if len(ind) == 0:
            warnings.warn("Couldn't cut the polygon in two")
            return Polygon(P)
        P1 = np.vstack((P[:(ind[0]+1),:], np.array(cut_point[0:2]).T, np.array(cut_point[2:4]).T, P[(ind[1]+1):, :]))
        P2 = np.vstack((np.array(cut_point[0:2]).T, P[(ind[0]+1):(ind[1]+1),:], np.array(cut_point[2:4]).T, np.array(cut_point[0:2]).T))
        return Polygon(P1), Polygon(P2)

def nGone(n):
    angle = 2 * np.pi * np.arange(n+1)/n
    P = np.array([np.cos(angle), np.sin(angle)])
    return Polygon(P.T)

def Intersec(P, p, ang):
    ux = P[0, 0]
    uy = P[0, 1]
    vx = P[1, 0]
    vy = P[1, 1]
    t = (p-ux*np.cos(ang)-uy*np.sin(ang))/((vx-ux)*np.cos(ang)+(vy-uy)*np.sin(ang))
    return t

def STIT(Poly, Stop_Time, Max_iter=500):
    Time = 0
    List_Poly = [Poly]
    List_Perimeter = [Poly.Perimeter()]
    Clock = [np.random.exponential(1/Poly.Perimeter())]
    nb_iter = 0
    while Time <= Stop_Time:
        index = np.argmin(Clock)
        Q = List_Poly.pop(index)
        _ = List_Perimeter.pop(index)
        t = Clock.pop(index)
        Time += t
        p, ang = Q.Simulate_Uniform()
        P1, P2 = Q.CutPoly(p, ang)
        per1 = P1.Perimeter()
        per2 = P2.Perimeter()
        List_Poly += [P1, P2]
        List_Perimeter += [per1, per2]
        Clock = [T-t for T in Clock]
        Clock += [np.random.exponential(1/per1), np.random.exponential(1/per2)]
        nb_iter += 1
        if nb_iter >= Max_iter:
            warnings.warn("Max iteration reached")
            break
    return List_Poly
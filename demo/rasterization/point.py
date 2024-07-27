__n_types__ = int | float
class Point2d:
    """Generic point in Cartesian space. Passing only one number will 
    create a point with the same x and y coordinates."""
    def __init__(self, x: __n_types__, y: __n_types__, dtype: object = int) -> None:
        self.x = dtype(x)
        self.y = dtype(y)

    def __lt__(self, v) -> bool:
        return (v.y < self.y) or (self.y == v.y and v.x < self.x)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Triangle:
    def __init__(self, p1: Point2d, p2: Point2d, p3: Point2d, sort: bool = True) -> None:
        self.p1, self.p2, self.p3 = p1, p2, p3
        if sort: self.sort()
    
    def sort(self) -> None:
        self.p1, self.p2, self.p3 = y_sort(self.p1, self.p2, self.p3)


__pt_arr__ = list[Point2d] | tuple[Point2d] 
def y_sort(*points: __pt_arr__, reverse: bool = False) -> list:
    """Sorts a list of points by their mantissa values. If that 
    value is equal, sort them by abscissa values instead. """
    return sorted(points, key=lambda p: (p.y, p.x), reverse=reverse)


def is_sorted(*points: __pt_arr__) -> bool:
    """Check if a list of 3 points is sorted by mantissa or not. """
    assert len(points) == 3, f'Needed 3 points as input, got {len(points)}.'
    return (not points.index(points[0])) and (points.index(points[2]) == 2);


def find(p1: Point2d, p2: Point2d, x = None, y = None) -> __n_types__:
    """Finds a coordinate lying on a line whose end points are p1 and p2, 
    given the other coordinate. For instance, if you pass the x-coordinate, 
    and set y to None, the missing y-coordinate will be the return value."""
    assert not ((x is None) and (y is None)), "Both x and y can not be None. "
    if x is None: return round(p2.x - ((p2.y - y) * (p2.x - p1.x) / (p2.y - p1.y)), 3)
    return round(p2.y - ((p2.x - x) * (p2.y - p1.y) / (p2.x - p1.x)), 3)


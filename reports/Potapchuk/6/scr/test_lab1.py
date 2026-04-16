import math
import pytest  
from lab1_functions import solve_quadratic  

def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == [1.0, 2.0]
    assert solve_quadratic(1, 2, 1) == [-1.0]
    assert solve_quadratic(1, 0, 1) == []
    with pytest.raises(ValueError):
        solve_quadratic(0, 1, 1)
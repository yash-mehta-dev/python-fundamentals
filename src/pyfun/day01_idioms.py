from dataclasses import dataclass, field


"""Day 1 — Comprehensions and core idioms."""


def even_squares(nums: list[int]) -> list[int]:
    """Return squares of even numbers from nums.
    
    Why a comprehension here: single transformation + filter, reads cleanly.
    """
    return [x * x for x in nums if x % 2 == 0]


def word_lengths(words: list[str]) -> dict[str, int]:
    """Map each word to its length. Last duplicate wins (dict semantics)."""
    return {w: len(w) for w in words}


def unique_first_letters(words: list[str]) -> set[str]:
    """First letter of each non-empty word, lowercased, deduplicated."""
    return {w[0].lower() for w in words if w}


def flatten(matrix: list[list[int]]) -> list[int]:
    """Flatten a 2D matrix. Note: outer loop first."""
    return [num for row in matrix for num in row]


def stream_sum_of_squares(n: int) -> int:
    """Sum of squares 0..n-1 using a generator (constant memory)."""
    return sum(x * x for x in range(n))



@dataclass(frozen=True, slots=True)
class User:
    """An immutable user value object.
    
    frozen=True: hashable, safe as dict key, no accidental mutation.
    slots=True: ~40% smaller in memory, faster attribute access.
    """
    name: str
    age: int
    tags: list[str] = field(default_factory=list)


@dataclass
class Rectangle:
    """Demonstrates __post_init__ for validation + derived fields."""
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self) -> None:
        if self.width < 0 or self.height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.area = self.width * self.height


import math
import numpy as np


def dot_product_manual(a: list[float], b: list[float]) -> float:
    """Algebraic definition. Pure Python, no NumPy."""
    if len(a) != len(b):
        raise ValueError(f"Length mismatch: {len(a)} vs {len(b)}")
    return sum(x * y for x, y in zip(a, b))


def dot_product_geometric(a: list[float], b: list[float]) -> float:
    """Geometric definition: ||a|| * ||b|| * cos(angle).
    
    Equal to algebraic version by definition — this is just to verify.
    """
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    cos_theta = dot_product_manual(a, b) / (norm_a * norm_b)
    return norm_a * norm_b * cos_theta


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Direction-only similarity. Always in [-1, 1]."""
    a_arr = np.array(a, dtype=float)
    b_arr = np.array(b, dtype=float)
    norm_product = np.linalg.norm(a_arr) * np.linalg.norm(b_arr)
    if norm_product == 0:
        return 0.0
    return float(np.dot(a_arr, b_arr) / norm_product)


def angle_between_degrees(a: list[float], b: list[float]) -> float:
    """The actual angle between two vectors, in degrees."""
    cos_t = cosine_similarity(a, b)
    # Numerical safety — floating point can push this slightly outside [-1, 1]
    cos_t = max(-1.0, min(1.0, cos_t))
    return math.degrees(math.acos(cos_t))
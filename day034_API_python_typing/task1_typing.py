age: int
name: str
height: float
is_human: bool


# Type hint "->" to show what is the expected output from a function
def police_check(person_age: int) -> bool:
    return person_age >= 18

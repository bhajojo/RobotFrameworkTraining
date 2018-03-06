def var_args(name ,**kwargs):
    print(name)
    print(kwargs["description"],kwargs["feedback"])


var_args("Mark",description="Loves  python", feedback="I am learning python")
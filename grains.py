
def grains_counter(squares):
    grains = 1
    if squares == 1:
        return grains
    else:
        for i in range(2, squares+1):
            grains = grains * 2
        return grains


print(grains_counter(64))

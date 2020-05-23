
def forward_checking(rv):
    for row in rv:
        if [] in row:
            return False

    return True

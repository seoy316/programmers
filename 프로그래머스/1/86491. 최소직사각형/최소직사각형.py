def solution(sizes):
    resizes = []

    w, h = 0, 0

    for size in sizes:
        if size[0] > size[1]:
            resizes.append([size[0], size[1]])
        else:
            resizes.append([size[1], size[0]])

    for re in resizes:
        if re[0] > w:
            w = re[0]

        if re[1] > h:
            h = re[1]

    return w * h

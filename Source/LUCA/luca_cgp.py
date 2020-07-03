


def define_input_cgp(cgp0, cgp1):
    output = [cgp0, cgp1]
    output[0] += 1
    return output


def define_output_cgp(cgp0, cgp1):
    output = [cgp0, cgp1]
    output[0] += 1
    return output


def define_cgp(cgp0, cgp1, row):
    output = [cgp0, cgp1]
    if cgp0 == row - 1:
        output[1] += 1
        output[0] = 0
    else:
        output[0] += 1
    return output
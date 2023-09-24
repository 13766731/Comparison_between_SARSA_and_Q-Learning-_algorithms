def plant(inpute,fault, reference):
    mean_input_refrence = 300.013641
    mean_output_reference = 18.292426
    inpute += fault
    a=reference.activate([inpute/mean_input_refrence])*mean_output_reference
    return (a)
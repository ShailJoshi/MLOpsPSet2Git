# Function to generate output with given over and wickets input and current params
import numpy


def RunProductionFn(input,params):
    u_arr = input[0].astype(float)
    w_arr = input[1]
    if len(u_arr.shape)>0:
        output = numpy.zeros_like(u_arr)
        for ii in range(len(u_arr)):
            u = u_arr[ii]
            w = int(w_arr[ii])
            if w!=10:
                output[ii] = params[w]*(1.0 - numpy.exp((-params[11]*u)/(params[w])))
            else:
                output[ii] = 0
    else:
        w_arr = int(w_arr)
        output = params[w_arr]*(1.0 - numpy.exp((-params[11]*u_arr)/(params[w_arr])))
    return output
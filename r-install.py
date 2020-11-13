import rpy2.robjects as ro


def main():

    R = ro.r

    R.source("environ.R")
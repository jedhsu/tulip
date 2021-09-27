class Histogram(StatisticalOperator):
    histogram = jnp.histogram
    histogram_bin_edges = jnp.histogram_bin_edges
    histogram2d = jnp.histogram2d
    histogramdd = jnp.histogramdd

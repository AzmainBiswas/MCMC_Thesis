def MetropolisSample(targer_function, init_state, step_size, sample_size=SAMPLESIZE):
    current_state = init_state
    samples = []
    for _ in range(sample_size):
        candidate_state = numpy.random.normal(loc=current_state, scale=step_size)  # jumping probability
        accept_prob = numpy.minimum(1.0, targer_function(candidate_state) / targer_function(current_state))  # acceptance probability
        if numpy.random.uniform() < accept_prob:
            current_state = candidate_state
        samples.append(current_state)
    return numpy.array(samples)

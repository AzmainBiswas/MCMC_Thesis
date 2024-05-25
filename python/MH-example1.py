import numpy as np
def MetropolisSample(pdf, init_state, step_size, sample_size=SAMPLESIZE):
    current_state = init_state
    samples = []
    for _ in range(sample_size):
        candidate_state = np.random.normal(loc=current_state, scale=step_size)  # jumping probabitlity
        accept_prob = np.minimum(1.0, pdf(candidate_state) / pdf(current_state))  # acceptance probability
        if np.random.uniform() < accept_prob:
            current_state = candidate_state
        samples.append(current_state)
    return np.array(samples)

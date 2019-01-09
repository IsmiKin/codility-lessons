
NUCLEOTIDE_TYPE_A = 'A'
NUCLEOTIDE_TYPE_C = 'C'
NUCLEOTIDE_TYPE_G = 'G'
NUCLEOTIDE_TYPE_T = 'T'

NUCLEOTIDE_IMPACT_FACTORS = {
    NUCLEOTIDE_TYPE_A: 1,
    NUCLEOTIDE_TYPE_C: 2,
    NUCLEOTIDE_TYPE_G: 3,
    NUCLEOTIDE_TYPE_T: 4
}


def prefix_sums(dna_sequence):
    # We create a matrix like
    # [A][0, 0, 0 ... (len dna)]
    # [C][0, 0, 0 ... (len dna)]
    # [G][0, 0, 0 ... (len dna)]
    # [T][0, 0, 0 ... (len dna)]
    sums = {}
    for type, impact_factor in NUCLEOTIDE_IMPACT_FACTORS.items():
        sums[type] = [0] * len(dna_sequence)

        # It will record the sum of type until that nucleotide,
        # it means, how many A, T, C, G are until position 4.. and then 5, etc..
        for index, nucleotide in enumerate(dna_sequence):
            sums[type][index] = sums[type][index - 1] + 1 if nucleotide == type else sums[type][index - 1]
    return sums


def total_one_slice(prefix_sums, start, end):
    return prefix_sums[end + 1] - prefix_sums[start]


def minimal_impact_factor_subsequence(prefix_sums, start, end):
    prefix_sum_range = {}
    # Get sums of each type in that range
    for type in NUCLEOTIDE_IMPACT_FACTORS.keys():
        prefix_sum_range[type] = total_one_slice(prefix_sums[type], start, end)

    # this can be done more elegant
    if prefix_sum_range['A'] > 0:
        return 1
    elif prefix_sum_range['C'] > 0:
        return 2
    elif prefix_sum_range['G'] > 0:
        return 3
    else:
        return 4


def minimal_impact_factor(dna_sequence, p, q):
    p_sums = prefix_sums(dna_sequence)
    result_queries = [None] * len(p)
    
    for query_index, (start, end) in enumerate(zip(p, q)):
        result_queries[query_index] = minimal_impact_factor_subsequence(p_sums, start, end)

    return result_queries

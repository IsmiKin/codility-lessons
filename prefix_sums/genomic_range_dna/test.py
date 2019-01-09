import pytest

from genomic_range_query import minimal_impact_factor


@pytest.mark.parametrize(
    'dna_sequence, p, q, expected',
    [
        (
            'CAGCCTA', [2, 5], [4, 5], [2, 1]
            # 'CAGCCTA', [2, 5, 0], [4, 5, 6], 1
        )
    ]
)
def test_equilibrium_naturals(dna_sequence, p, q, expected):
    assert expected == minimal_impact_factor(dna_sequence, p, q)

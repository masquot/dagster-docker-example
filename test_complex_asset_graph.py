import complex_asset_graph as cag

def test_nabisco_cereals():
    cereals = [
        {"name": "cereal1", "mfr": "N"},
        {"name": "cereal2", "mfr": "K"},
    ]
    result = cag.nabisco_cereals(cereals)
    assert len(result) == 1
    assert result == [{"name": "cereal1", "mfr": "N"}]


from dagster import materialize


def test_cereal_assets():
    assets = [
        cag.nabisco_cereals,
        cag.cereals,
        cag.cereal_protein_fractions,
        cag.highest_protein_nabisco_cereal,
    ]

    result = materialize(assets)
    assert result.success
    assert result.output_for_node("highest_protein_nabisco_cereal") == "100% Bran"


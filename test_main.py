from main import aduna, genereaza_mesaj

def test_aduna():
    assert aduna(2, 3) == 5
    assert aduna(-1, 1) == 0

def test_genereaza_mesaj():
    assert genereaza_mesaj("Corina") == "Bun venit, Corina!"
    assert "Bun venit" in genereaza_mesaj("Andrei")
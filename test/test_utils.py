import os
import shutil

from src.utils import (
    remove_host_from_url,
    save_df_to_csv,
    check_poligon,
    POLYGON_ESCALADA,
)


def teardown_function(function):
    if os.path.exists("data"):
        shutil.rmtree("data")


def test_remove_host_from_url():
    url = "https://www.google.com/test"
    assert remove_host_from_url(url) == "test"


def test_save_df_to_csv(df_estates):
    filename = "data/test.csv"
    save_df_to_csv(df_estates, filename)
    assert os.path.exists(filename)


def test_check_polygon():
    fuera = []
    dentro = []
    fuera_escalada_norte_oeste = (-34.7144, -58.3994)
    fuera_escalada_banfield = (-34.7338, -58.4063)
    fuera_escalada_norte_este = (-34.7153, -58.3936)
    fuera.append(fuera_escalada_norte_oeste)
    fuera.append(fuera_escalada_banfield)
    fuera.append(fuera_escalada_norte_este)
    dentro_escalada_centro = (-34.7235, -58.3982)
    dentro_escalada_borde_sur_oeste = (-34.7374, -58.4048)
    dentro_escalada_borde_norte_oeste = (-34.7150, -58.3997)
    dentro.append(dentro_escalada_centro)
    dentro.append(dentro_escalada_borde_sur_oeste)
    dentro.append(dentro_escalada_borde_norte_oeste)
    for lat, long in fuera:
        assert not check_poligon(lat, long)

    for lat, long in dentro:
        assert check_poligon(lat, long)

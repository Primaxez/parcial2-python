from fastapi import FastAPI, status
from fastapi.testclient import TestClient

class TestArtistRoutes:
    #probar que las rutas de artista existen
    def test_route_get_all_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("artists:get-all-artists"))
        assert res.status_code != status.HTTP_404_NOT_FOUND

    def test_route_get_albums_by_id_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("artists:get-albums-by-artist-id", id=1))
        assert res.status_code != status.HTTP_404_NOT_FOUND

    def test_route_get_tracks_by_id_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("artists:get-tracks-by-artist-id", id=1))
        assert res.status_code != status.HTTP_404_NOT_FOUND
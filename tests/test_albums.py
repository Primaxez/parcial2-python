from fastapi import FastAPI, status
from fastapi.testclient import TestClient

class TestAlbumRoutes:
    #probar que las rutas de album existen
    def test_route_get_tracks_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("albums:get-tracks-in-album", id=1))
        assert res.status_code != status.HTTP_404_NOT_FOUND
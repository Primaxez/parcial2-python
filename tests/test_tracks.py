from fastapi import FastAPI, status
from fastapi.testclient import TestClient

class TestTrackRoutes:
    #probar que las rutas de track existen
    def test_route_get_track_by_id_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("tracks:get-track-by-id", id=1))
        assert res.status_code != status.HTTP_404_NOT_FOUND
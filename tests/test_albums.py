"""
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
import pytest

class TestAlbumRoutes:
    #test routes exist
    def test_routes_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("albums:get-albums"))
        assert res.status_code != status.HTTP_404_NOT_FOUND

class TestGetAlbumTracks:
    #test routes exist
    def test_routes_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("albums:get-album-tracks"))
        assert res.status_code != status.HTTP_404_NOT_FOUND
"""
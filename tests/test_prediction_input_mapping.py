import app as student_app


def test_prediction_route_preserves_reading_and_writing_scores(monkeypatch):
    captured = {}

    class FakePipeline:
        def predict(self, features):
            captured.update(features.iloc[0].to_dict())
            return [72.5]

    monkeypatch.setattr(student_app, "PredictPipeline", FakePipeline)
    client = student_app.app.test_client()

    response = client.post(
        "/predictdata",
        data={
            "gender": "female",
            "ethnicity": "group C",
            "parental_level_of_education": "some college",
            "lunch": "standard",
            "test_preparation_course": "completed",
            "reading_score": "81",
            "writing_score": "74",
        },
    )

    assert response.status_code == 200
    assert captured["reading_score"] == 81.0
    assert captured["writing_score"] == 74.0
    assert b"72.5" in response.data

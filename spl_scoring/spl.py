"""SPL: accumulates weighted phishing indicators for one URL and maps the
total score to a human-readable danger level."""


class SPL:
    """Collects weighted findings and derives the overall risk level."""

    def __init__(self):
        self.score = 0
        self.reasons = []

    def add(self, points, reason):
        """Record one finding: `points` added to the score, `reason` shown to the user."""
        self.score += points
        self.reasons.append(reason)

    def get_danger_level(self):
        """Map the total score to a qualitative risk level."""
        if self.score >= 100:
            return "CRITICAL"
        elif self.score >= 75:
            return "Very high"
        elif self.score >= 50:
            return "Medium"
        elif self.score >= 25:
            return "Low"
        elif self.score >= 1:
            return "Very low"
        else:
            return "Non detect"

from __future__ import annotations

import unittest

from tools import verify_public_surface


class PublicSurfaceTests(unittest.TestCase):
    def test_private_repository_reference_is_rejected(self) -> None:
        data = ("realiserings" + "grammatikk-artifact-family").encode()
        self.assertIn(
            "PRIVATE_REPOSITORY_REFERENCE",
            verify_public_surface.classify_data(data),
        )

    def test_provider_token_is_rejected(self) -> None:
        data = ("gh" + "p_" + "A" * 24).encode()
        self.assertIn("CREDENTIAL_MATERIAL", verify_public_surface.classify_data(data))

    def test_public_architectural_prose_is_allowed(self) -> None:
        self.assertEqual(
            verify_public_surface.classify_data(
                b"Candidate does not equal consequence. No physical authority."
            ),
            set(),
        )


if __name__ == "__main__":
    unittest.main()

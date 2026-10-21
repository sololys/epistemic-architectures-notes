# MORANDI-CORE // FORMAL REALIZATION CONTRACT (epistemic-architectures-notes)
# Default target is FAIL-CLOSED (0.00 V DC). Explicit verification is mandatory.

.DEFAULT_GOAL := hold
.PHONY: hold verify

hold:
	@echo "[HOLD] 0.00 V DC. System is at rest. Run 'make verify' to execute L1-L3 proof chains and notes surface checks."
	@exit 1

verify:
	@python3 -m unittest -q L1_LAW/invariants_pure.py
	@python3 L2_GATE/evaluate_boundaries.py
	@python3 tools/verify_cos45_kms_spectral_series.py
	@python3 tools/verify_public_surface.py
	@python3 -m unittest -q tools/test_verify_public_surface.py
	@echo "[L1_VERIFIED // HOLD_READY_FOR_W2] L1 software checks passed (PHYSICAL_AUTHORITY=NONE; W_human required for W2). All spectral invariants and public surface bounds satisfied."

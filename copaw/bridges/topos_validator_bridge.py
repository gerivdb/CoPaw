#!/usr/bin/env python3
"""
CoPaw TOPOS Validator Bridge v1.0
Validates TOPOS environment profiles against schema.

Bridge: TOPOS-COPAW-VALIDATION (active - consumer side)
IntentHash: 0xTOPOS_COPAW_BRIDGE_20260603
"""

__version__ = "1.0.0"

import json
import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

REQUIRED_PROFILE_FIELDS = ["env", "topos_version", "repos"]
REQUIRED_REPO_FIELDS = ["name", "status"]


class ToposValidatorBridge:
    """Validates TOPOS environment profiles against schema/topos_v1.yaml."""

    def __init__(self):
        self._validated: List[Dict] = []
        self._errors: List[Dict] = []

    def validate_profile(self, profile_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate a TOPOS environment profile."""
        errors = []
        warnings = []

        # Check required fields
        for field in REQUIRED_PROFILE_FIELDS:
            if field not in profile_data:
                errors.append(f"Missing required field: {field}")

        repos = profile_data.get("repos", [])
        if not repos:
            warnings.append("No repos in profile")

        valid_repos = 0
        for repo in repos:
            repo_errors = []
            for field in REQUIRED_REPO_FIELDS:
                if field not in repo:
                    repo_errors.append(f"Repo missing field: {field}")
            if repo_errors:
                errors.extend(repo_errors)
            else:
                valid_repos += 1

        coverage = valid_repos / max(len(repos), 1)

        result = {
            "env": profile_data.get("env", "unknown"),
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "repos_total": len(repos),
            "repos_valid": valid_repos,
            "coverage": round(coverage, 3)
        }

        self._validated.append(result)
        if errors:
            self._errors.append(result)

        logger.info("CoPaw validated profile: env=%s, valid=%s, coverage=%.2f",
                     result["env"], result["valid"], coverage)
        return result

    @property
    def validated_count(self) -> int:
        return len(self._validated)

    @property
    def error_count(self) -> int:
        return len(self._errors)

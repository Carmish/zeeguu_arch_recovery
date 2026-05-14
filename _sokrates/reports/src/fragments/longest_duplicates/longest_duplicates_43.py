zeeguu/core/mwe/llm_mwe_detector.py [255:288]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def _validate_groups(self, data: List, num_tokens: int) -> List[Dict]:
        """Validate and filter MWE groups."""
        if not isinstance(data, list):
            return []

        valid_groups = []
        for group in data:
            if not isinstance(group, dict):
                continue

            head_idx = group.get("head_idx")
            dependent_indices = group.get("dependent_indices", [])
            mwe_type = group.get("type", "unknown")

            # Validate indices
            if not isinstance(head_idx, int) or not (0 <= head_idx < num_tokens):
                continue

            if not isinstance(dependent_indices, list):
                continue

            valid_deps = [
                idx for idx in dependent_indices
                if isinstance(idx, int) and 0 <= idx < num_tokens and idx != head_idx
            ]

            if valid_deps:
                valid_groups.append({
                    "head_idx": head_idx,
                    "dependent_indices": valid_deps,
                    "type": mwe_type
                })

        return valid_groups
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




"""
This module represents the behavior of a semantic analyzer for the Interactive Story Compiler.

Author: Laura Beltrán & Santiago Sánchez
"""

class SemanticAnalyzer:
    """Semantic Analyzer: builds internal representation, validates references."""

    def __init__(self, tokens_input):
        self.tokens = tokens_input
        self.scenes = {}
        self.defined_scene_ids = set()
        self.referenced_scene_ids = set()

    def analyze(self):
        i = 0
        n = len(self.tokens)

        while i < n:
            # Expect: scene : IDENTIFIER
            if not self._match(i, "KEYWORD", "scene"):
                i += 1
                continue
            if not self._match(i + 1, "SYMBOL", ":"):
                raise Exception("Expected ':' after 'scene'")
            if not self._match(i + 2, "IDENTIFIER"):
                raise Exception("Expected scene identifier after 'scene:'")

            scene_id = self.tokens[i + 2].value
            self.defined_scene_ids.add(scene_id)
            i += 3

            # Expect: text : "..."
            if not self._match(i, "KEYWORD", "text"):
                raise Exception(f"Expected 'text' in scene {scene_id}")
            if not self._match(i + 1, "SYMBOL", ":"):
                raise Exception(f"Expected ':' after 'text' in scene {scene_id}")
            if not self._match(i + 2, "STRING"):
                raise Exception(f"Expected STRING after text: in scene {scene_id}")
            scene_text = self.tokens[i + 2].value.strip('"')
            i += 3

            # Create scene entry
            self.scenes[scene_id] = {"text": scene_text, "choices": []}

            # Handle zero or more choices
            while i < n and self._match(i, "KEYWORD", "choice"):
                if not self._match(i + 1, "SYMBOL", ":"):
                    raise Exception("Expected ':' after 'choice'")
                if not self._match(i + 2, "STRING"):
                    raise Exception("Expected STRING after choice:")
                if not self._match(i + 3, "SYMBOL", "->"):
                    raise Exception("Expected '->' after choice string")
                if not self._match(i + 4, "IDENTIFIER"):
                    raise Exception("Expected destination scene identifier after '->'")

                choice_text = self.tokens[i + 2].value.strip('"')
                destination = self.tokens[i + 4].value
                self.referenced_scene_ids.add(destination)

                self.scenes[scene_id]["choices"].append({
                    "text": choice_text,
                    "destination": destination
                })
                i += 5

        # Semantic validation
        if "START" not in self.defined_scene_ids:
            raise Exception("Missing START scene. Every story must begin with scene: START")

        undefined_destinations = self.referenced_scene_ids - self.defined_scene_ids
        if undefined_destinations:
            raise Exception(f"Undefined scene destinations: {undefined_destinations}")

        # Unreachable scenes check
        graph = {
            scene: [choice["destination"] for choice in data["choices"]]
            for scene, data in self.scenes.items()
        }

        reachable = set()

        def dfs(scene_id):
            if scene_id in reachable:
                return
            reachable.add(scene_id)
            for neighbor in graph.get(scene_id, []):
                dfs(neighbor)

        dfs("START")

        unreachable = self.defined_scene_ids - reachable
        if unreachable:
            raise Exception(f"Unreachable scenes detected: {unreachable}")

        return self.scenes

    def _match(self, i, expected_type, expected_value=None):
        """Checks if token i matches type and optional value."""
        if i >= len(self.tokens):
            return False
        token = self.tokens[i]
        if token.type != expected_type:
            return False
        if expected_value is not None and token.value != expected_value:
            return False
        return True
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
            token = self.tokens[i]
            if token.type == "SCENE":
                # Parse scene header
                if i+1 >= n or self.tokens[i+1].type != "IDENTIFIER":
                    raise Exception("Expected IDENTIFIER after SCENE")
                scene_id = self.tokens[i+1].value
                self.defined_scene_ids.add(scene_id)
                i += 2

                # Parse text
                if i >= n or self.tokens[i].type != "TEXT":
                    raise Exception(f"Expected TEXT in scene {scene_id}")
                i += 1

                if i >= n or self.tokens[i].type != "STRING":
                    raise Exception(f"Expected STRING after TEXT in scene {scene_id}")
                scene_text = self.tokens[i].value.strip('"')
                i += 1

                # Prepare scene entry
                self.scenes[scene_id] = {"text": scene_text, "choices": []}

                # Parse optional choices
                while i < n and self.tokens[i].type == "CHOICE":
                    i += 1
                    if i >= n or self.tokens[i].type != "STRING":
                        raise Exception("Expected STRING after CHOICE")
                    choice_text = self.tokens[i].value.strip('"')
                    i += 1

                    if i >= n or self.tokens[i].type != "ARROW":
                        raise Exception("Expected '->' after choice text")
                    i += 1

                    if i >= n or self.tokens[i].type != "IDENTIFIER":
                        raise Exception("Expected destination IDENTIFIER after '->'")
                    destination = self.tokens[i].value
                    self.referenced_scene_ids.add(destination)

                    self.scenes[scene_id]["choices"].append(
                        {"text": choice_text, "destination": destination}
                    )
                    i += 1
            else:
                i += 1

        # Semantic validation: check for undefined destinations
        undefined_destinations = self.referenced_scene_ids - self.defined_scene_ids
        if undefined_destinations:
            raise Exception(f"Undefined scene destinations: {undefined_destinations}")

        # Check for unreachable scenes (scene is defined but never reached)
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

        if "START" not in self.defined_scene_ids:
            raise Exception("Missing START scene. Every story must begin with scene: START")

        dfs("START")

        unreachable = self.defined_scene_ids - reachable
        if unreachable:
            raise Exception(f"Unreachable scenes detected: {unreachable}")

        return self.scenes

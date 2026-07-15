class ExecutionPlanner:

    def create_plan(self, intent: str):

        plans = {

            "video": [
                "Workflow Agent",
                "Video Engine"
            ],

            "voice": [
                "Workflow Agent",
                "Voice Engine"
            ],

            "general": [
                "System Agent"
            ]
        }

        return plans.get(intent, ["System Agent"])
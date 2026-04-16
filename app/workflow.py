from temporalio import workflow


@workflow.defn
class Workflow:
    @workflow.run
    async def run(self) -> str:
        return ""

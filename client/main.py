import asyncio
import uuid

from temporalio.client import Client

from app.constants import SERVER_ADDR, TASK_QUEUE
from app.workflow import Workflow


async def main() -> None:
    client = await Client.connect(SERVER_ADDR)

    handle = await client.start_workflow(
        Workflow.run,
        id=str(uuid.uuid4()),
        task_queue=TASK_QUEUE,
    )

    print(
        f"started workflow: WorkflowID={handle.id} RunID={handle.first_execution_run_id}"
    )

    result = await handle.result()
    print(f"workflow result: {result}")


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())

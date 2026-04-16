import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from app.constants import SERVER_ADDR, TASK_QUEUE
from app.workflow import Workflow


async def main() -> None:
    client = await Client.connect(SERVER_ADDR)

    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[Workflow],
    )

    await worker.run()


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())

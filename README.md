# temporal-s3-python
Starter for Temporal S3 driver

## Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Temporal CLI](https://docs.temporal.io/cli#install)
- [uv](https://docs.astral.sh/uv/)

## Setup

Install dependencies using [uv](https://docs.astral.sh/uv/):

```sh
uv pip install -e .
```

## Running

### 1. Start the Temporal dev server

```sh
temporal server start-dev
```

This starts a local Temporal server on `localhost:7233` and the Web UI at `http://localhost:8233`.

### 2. Start the worker

In a separate terminal:

```sh
uv run worker
```

The worker registers the `Workflow` and polls `task-queue` for tasks.

### 3. Run the client

In another terminal:

```sh
uv run client
```

The client starts a new workflow execution with a random ID, waits for it to complete, and prints the result.

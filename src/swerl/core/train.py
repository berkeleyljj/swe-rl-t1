from datasets import load_dataset
import asyncio
from litellm import completion, acompletion
from litellm.exceptions import (
    BadRequestError,
    RateLimitError,
    ServiceUnavailableError,
    InvalidRequestError,
    AuthenticationError,
)

# Use dataset from SWE-Gym as training data
dataset = load_dataset("SWE-Gym/SWE-Gym", split="train")

#TODO: Add training script
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
from trl import GRPOTrainer, ModelConfig, ScriptArguments, TrlParser, get_peft_config

# Use dataset from SWE-Gym as training data
training_data = load_dataset("SWE-Gym/SWE-Gym", split="train")


#TODO: Prompt the model to generate patch

#TODO: Add training script
trainer = GRPOTrainer(
    model="QwQ-32B",
    reward_funcs=reward_funcs,
    args=training_args,
    train_dataset=training_data,
    peft_config=get_peft_config(model_args),
    callbacks=get_callbacks(training_args, model_args),
    processing_class=tokenizer,
)